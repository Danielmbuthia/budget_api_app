from django.urls import path

from .views import *


urlpatterns = [
    path('category/',IncomeCategoryListView.as_view(),name='category'),
    path('category/<str:pk>/',IncomeCategoryDetailAPiView.as_view(),name='category_detail'),
    path('<str:pk>/',IncomeDetailAPIView.as_view(),name='income_detail'),
    path('',IncomeListAPIView.as_view(),name='income'),
]
