from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import ExpenseCategory, Expense
from .permission import IsOwner
from .serializer import ExpenseCategorySerializer, ExpenseSerializer
from rest_framework import permissions


class ExpenseCategoryListAPiView(ListCreateAPIView):
    serializer_class = ExpenseCategorySerializer
    queryset = ExpenseCategory.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class ExpenseCategoryDetailAPiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseCategorySerializer
    queryset = ExpenseCategory.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'


class ExpenseListAPIView(ListCreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    lookup_field = 'id'

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
