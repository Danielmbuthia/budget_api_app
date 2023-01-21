from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import ExpenseCategory
from .serializer import ExpenseCategorySerializer
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
