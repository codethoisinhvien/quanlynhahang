import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.db.models import Sum

from src.models import BillDetail, ChefBill, Bill
from src.serializers.bill_detail_serializer import BillDetailSerializer
from src.serializers.bill_serializer import BillDetailMoreSerializer
from src.serializers.chef_bill_serializer import ChefBillSerializer
from src.serializers.food_serializer import BestFoodSerializer


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = self.room_name
        print(self.room_group_name)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        if self.room_name == "chef":
            best_food = self.conention_query()
            print(best_food)
            best_food_serializer = BestFoodSerializer(best_food, many=True)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': best_food_serializer.data
                }
            )
        elif self.room_name == "delivery":
            query = ChefBill.objects.all()
            chef_bill_serializer = ChefBillSerializer(query, many=True)
            await self.channel_layer.group_send(
                "delivery",
                {
                    'type': 'chat_message_delivery',
                    'message': chef_bill_serializer.data
                }
            )
        elif self.room_name == "payment":
            bill = Bill.objects.all()
            a = BillDetailMoreSerializer(bill, many=True)
            await self.channel_layer.group_send(
                "payment",
                {
                    'type': 'chat_message',
                    'message': a.data
                }
            )

    def conention_query(self):

        return BillDetail.objects.values('food__name', 'food') \
            .order_by('food').annotate(count=Sum('amount'), count_complete=Sum(
            'amount_complete')).filter()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        data = text_data_json['data']
        print(self.room_name == "order")
        if self.room_name == "order":
            bill_detail_serializer = BillDetailSerializer(data=data, many=True)
            if bill_detail_serializer.is_valid():
                bill_detail_serializer.save()

                await self.send(text_data=json.dumps(
                    {"success": True, "type": "confirm", 'bill_detail': bill_detail_serializer.data},
                    ensure_ascii=False

                ))
            else:
                print(bill_detail_serializer.error_messages)
                await self.send(text_data=json.dumps(
                    {"success": False, "type": "confirm", 'message': "cos loi"},
                    ensure_ascii=False

                ))

            best_food = BillDetail.objects.values('food__name', 'food') \
                .order_by('food').annotate(count=Sum('amount'),
                                           count_complete=Sum(
                                               'amount_complete')).filter()
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
            chef_bill_serializer = ChefBillSerializer(query, many=True)
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
        elif self.room_name == "delivery":
            id = data['id']
            print(data)
            query = ChefBill.objects.get(pk=id)
            if query.status == True:
                query.status = False
                query.delivery_by = data['delivery_by']
                query.save()
            query2 = ChefBill.objects.all()
            chef_bill_serializer = ChefBillSerializer(query2, many=True)
            await self.channel_layer.group_send(
                "delivery",
                {
                    'type': 'chat_message_delivery',
                    'message': chef_bill_serializer.data
                }
            )

    async def chat_message(self, event):
        print(event)
        message = event['message']
        print("chef")
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "type": "chef",
            'message': message
        }, ensure_ascii=False))

    async def chat_message_delivery(self, event):
        print(event)
        message = event['message']
        print("chef")
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "type": "delivery",
            'message': message
        }, ensure_ascii=False))


def chef_cook(data):
    print(data)
    amount = data["amount"]
    queryset = BillDetail.objects.all().filter(food=data["food"])
    if len(queryset) > 0:
        print(queryset)
        i = 1
        while amount > 0:
            if queryset[i].amount > queryset[i].amount_complete:
                chef_bill = ChefBill()
                chef_bill.bill_detail = queryset[i]
                if amount > (queryset[i].amount - queryset[i].amount_complete):
                    queryset[i].amount_complete = queryset[i].amount
                    amount = amount - queryset[i].amount
                    chef_bill.amount = queryset[i].amount
                else:
                    queryset[i].amount_complete = queryset[i].amount_complete + amount
                    chef_bill.amount = amount
                    amount = 0
                print(chef_bill)
                chef_bill.save()
                # queryset[i].save()
                print(chef_bill)
                i = i + 1
                if i > len(queryset):
                    break
        print(queryset[i].amount_complete, queryset[i].amount_complete)

