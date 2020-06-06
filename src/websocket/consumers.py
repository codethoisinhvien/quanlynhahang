import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.db.models import Sum

from src.models import BillDetail
from src.serializers.food_serializer import BestFoodSerializer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        if self.room_name == "order":
            best_food = BillDetail.objects.values('food__name', 'food') \
                .order_by('food').annotate(count=Sum('amount'), count_complete=Sum('amount_complete')).filter()
            best_food_serializer = BestFoodSerializer(best_food, many=True)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': best_food_serializer.data
                }
            )
        elif self.room_name == "delivery":
            pass

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        # print(text_data)
        best_food = BillDetail.objects.values('food__name', 'food') \
            .order_by('food').annotate(count=Sum('amount'), count_complete=Sum('amount_complete')).filter()
        print(best_food)
        best_food_serializer = BestFoodSerializer(best_food, many=True)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': best_food_serializer.data
            }
        )

    async def chat_message(self, event):
        message = event['message']
        print(message)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "type": "chef",
            'message': message
        }, ensure_ascii=False))
