from authentication.serializers import UserSerializer
from income.models import Income, IncomeCategory
from rest_framework import serializers

class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = ('id', 'name', 'created_at', 'updated_at')
        
        
class IncomeSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=IncomeCategory.objects.all(),
                                                     write_only=True)
    category = IncomeCategorySerializer(required=False)
    owner = UserSerializer(required=False)

    def create(self, validated_data):
        category_data = validated_data.pop('category_id')
        income = Income.objects.create(category=category_data, **validated_data)
        return income

    class Meta:
        model = Income
        fields = ('id', 'category', 'owner','amount','description','category_id','created_at', 'updated_at')
        
