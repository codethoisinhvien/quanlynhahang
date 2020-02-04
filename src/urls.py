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
from src.apis.table_api import TableApi
from src.apis.table_group_api import TableGroupApi
from src.apis.customer_api import CustomersAPI
from src.apis.bill_api import BillAPI
from src.apis.bill_detail_api import BillDetail
urlpatterns = [
    path(r'food-group', FoodGroupApi.as_view(), name='food-group'),
    path(r'food-group/<int:id>', FoodGroupApi.as_view(), name='food-group'),
    path(r'foods', FoodApi.as_view(), name='foods'),
    path(r'table-groups', TableGroupApi.as_view(), name='tabele-groups'),
    path(r'table-groups/<int:id>', TableGroupApi.as_view(), name='table-group'),
    path(r'tables', TableApi.as_view(), name='table-group'),
    path(r'tables/<int:id>', TableApi.as_view(), name='table-group'),
    path(r'customers', CustomersAPI.as_view(), name='customers'),
    path(r'customer/<int:id>', TableApi.as_view(), name='customer'),
    path(r'bill', BillAPI.as_view(), name='bill'),
    path(r'bill-detail', BillDetail.as_view(), name='bill'),
    path(r'bill-detail/<int:id>', BillDetail.as_view(), name='bill'),

]
