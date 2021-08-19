from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.StoreList.as_view()),
    path('store/<str:pk>/', views.StoreDetail.as_view()),
]