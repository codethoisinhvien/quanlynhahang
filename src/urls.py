"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from src.apis import FoodGroupApi, FoodApi
from src.apis.authentication import AuthenticationApi
from src.apis.bill_api import BillsAPI, BillAPI
from src.apis.bill_detail_api import BillDetail
from src.apis.chef_bill_api import ChefBillApi
from src.apis.customer_api import CustomersAPI
from src.apis.food_api import BestFood
from src.apis.office_api import OfficeApi
from src.apis.statistic_api import StatisticApi
from src.apis.table_api import TablesApi,TableApi
from src.apis.table_group_api import TableGroupApi
from src.apis.user_api import UsersApi, UserApi

urlpatterns = [
    path(r'login', AuthenticationApi.as_view(), name='authentication'),
    path(r'food-group', FoodGroupApi.as_view(), name='food-group'),
    path(r'food-group/<int:id>', FoodGroupApi.as_view(), name='food-group'),
    path(r'users', UsersApi.as_view(), name='users'),
    path(r'users/<int:id>', UserApi.as_view(), name='user'),
    path(r'foods/', FoodApi.as_view(), name='foods'),
    path(r'foods/<int:id>', FoodApi.as_view(), name='foods'),
    path(r'table-groups', TableGroupApi.as_view(), name='tabele-groups'),
    path(r'table-groups/<int:id>', TableGroupApi.as_view(), name='table-group'),
    path(r'tables', TablesApi.as_view(), name='table-group'),
    path(r'tables/<int:id>', TablesApi.as_view(), name='table-group'),
    path(r'tables/<int:table_id>/bills', TableApi.as_view(), name='table-group'),
    path(r'customers', CustomersAPI.as_view(), name='customers'),
    path(r'customer/<int:id>', TablesApi.as_view(), name='customer'),
    path(r'bills', BillsAPI.as_view(), name='bills'),
    path(r'bills/<int:id>', BillAPI.as_view(), name='bill'),
    path(r'bill-detail', BillDetail.as_view(), name='bill'),
    path(r'bill-detail/<int:id>', BillDetail.as_view(), name='bill'),
    path(r'offices', OfficeApi.as_view(), name='bill'),
    path(r'best-food', BestFood.as_view(), name='bill'),
    path(r'chef-bill/<int:id>', ChefBillApi.as_view(), name='bill'),
    path(r'statistic', StatisticApi.as_view(), name='bill'),
]
