from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from expense.permission import IsOwner
from .serializer import IncomeCategorySerializer, IncomeSerializer

from .models import Income, IncomeCategory

# Create your views here.

class IncomeCategoryListView(ListCreateAPIView):
    serializer_class = IncomeCategorySerializer
    queryset = IncomeCategory.objects.all()
    permission_classes = [permissions.IsAuthenticated,]
    

class IncomeCategoryDetailAPiView(RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeCategorySerializer
    queryset = IncomeCategory.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'


class IncomeListAPIView(ListCreateAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class IncomeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    lookup_field = 'id'

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
