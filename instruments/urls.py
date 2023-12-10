from django.urls import path
from .views import InstrumentList, InstrumentDetail, OrderList, OrderDetail

urlpatterns = [
    path('instruments/', InstrumentList.as_view(), name='instrument-list'),
    path('instruments/<int:pk>/', InstrumentDetail.as_view(), name='instrument-detail'),
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
]
