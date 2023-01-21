from django.urls import path

from .views import ExpenseCategoryListAPiView, ExpenseCategoryDetailAPiView

urlpatterns = [
    path('', ExpenseCategoryListAPiView.as_view(), name='expense_categories'),
    path('<str:id>', ExpenseCategoryDetailAPiView.as_view(), name='expense_category')
]
