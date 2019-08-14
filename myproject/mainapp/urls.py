from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   # path('choice/<int:category_id>',views.choice, name='choice'),
    #path('detail/<int:product_id>',views.detail, name='detail'),
    path('mypage/',views.mypage, name="mypage"),
    path('buy/<int:product_id>',views.buy,name='buy'),
    path('pay/<int:product_id>',views.pay,name='pay'),
    path('detail/<int:product_id>/auction',views.auction, name='auction'),
    path('about/',views.about,name='about'),
    path('pay/<int:product_id>/delete', views.delete, name='delete'),
    
]