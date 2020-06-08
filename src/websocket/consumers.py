import json
from itertools import product

from channels.generic.websocket import AsyncWebsocketConsumer
from django.db.models import Sum

from src.models import BillDetail, ChefBill
from src.serializers.bill_detail_serializer import BillDetailSerializer
from src.serializers.chef_bill_serializer import ChefBillSerializer
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
        if self.room_name == "chef":
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
        text_data_json = json.loads(text_data)
        data = text_data_json['data']
        print(text_data_json)

        if self.room_name == "order":
            bill_detail_serializer = BillDetailSerializer(data=data, many=True)
            if bill_detail_serializer.is_valid():
                bill_detail_serializer.save()
                print("thanh cong")
                await self.send(text_data=json.dumps(
                    {"success": True, "type": "confirm", 'bill_detail': bill_detail_serializer.data},
                    ensure_ascii=False

                ))
            best_food = BillDetail.objects.values('food__name', 'food') \
                .order_by('food').annotate(count=Sum('amount'), count_complete=Sum('amount_complete')).filter()
            best_food_serializer = BestFoodSerializer(best_food, many=True)
            await self.channel_layer.group_send(
                "chef",
                {
                    'type': 'chat_message',
                    'message': best_food_serializer.data
                }
            )

        elif self.room_name == "chef":
            chef_cook(data)
            query = ChefBill.objects.all()
            chef_bill_serializer = ChefBillSerializer(query,many=True)
            print(chef_bill_serializer.data)
            await self.channel_layer.group_send(
                "delivery",
                {
                    'type': 'chat_message',
                    'message': chef_bill_serializer.data
                }
            )
            await self.send(text_data=json.dumps(
                {"success": True, "type": "confirm", 'bill_detail': "món ăn"},
                ensure_ascii=False

            ))

    async def chat_message(self, event):
        message = event['message']
        print(message)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "type": "chef",
            'message': message
        }, ensure_ascii=False))


def chef_cook(data):
    print(data["food"])
    amount = data["amount"]
    queryset = BillDetail.objects.all().filter(food=int(data["food"]))
    if len(queryset) > 0:
        print(queryset)
        i = 1

        if queryset[i].amount > queryset[i].amount_complete:
            chef_bill = ChefBill()
            chef_bill.bill_detail = queryset[i]
            if amount > (queryset[i].amount - queryset[i].amount_complete):
                # queryset[i].amount_complete = queryset[i].amount
                amount = amount - queryset[i].amount
                chef_bill.amount = queryset[i].amount
            else:
                # queryset[i].amount_complete = queryset[i].amount_complete + amount
                chef_bill.amount = amount
                amount = 0
            print(chef_bill)
            chef_bill.save()
            # queryset[i].save()
        print(queryset[0].amount_complete, queryset[0].amount_complete)

        # while amount>0:
