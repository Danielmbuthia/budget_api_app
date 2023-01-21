from django.urls import path

from .views import ExpenseCategoryListAPiView, ExpenseCategoryDetailAPiView, ExpenseListAPIView, ExpenseDetailAPIView

urlpatterns = [
    path('category', ExpenseCategoryListAPiView.as_view(), name='expense_categories'),
    path('category/<str:id>', ExpenseCategoryDetailAPiView.as_view(), name='expense_category'),
    path('', ExpenseListAPIView.as_view(), name='expenses'),
    path('<str:id>', ExpenseDetailAPIView.as_view(), name='expense'),
]
