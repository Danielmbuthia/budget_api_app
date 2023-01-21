from rest_framework import serializers
from authentication.serializers import UserSerializer
from .models import ExpenseCategory, Expense


class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ['id', 'name', 'created_at']


class ExpenseSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=ExpenseCategory.objects.all(),
                                                     write_only=True)
    category = ExpenseCategorySerializer(required=False)
    owner = UserSerializer(required=False)

    def create(self, validated_data):
        category_data = validated_data.pop('category_id')
        expense = Expense.objects.create(category=category_data, **validated_data)
        return expense

    class Meta:
        model = Expense
        fields = ['id', 'amount', 'description', 'category_id', 'owner', 'category', 'created_at']
