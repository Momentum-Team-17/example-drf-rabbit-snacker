from rest_framework import serializers
from .models import Food, Rabbit


# non-DRF DIY serializer
class RabbitDIYSerializer():
    def __init__(self, instance):
        self.instance = instance

    class Meta:
        Rabbit

    def serialize(self):
        rabbit_as_dict = {
            'pk': self.instance.pk,
            'name': self.instance.name,
        }
        return rabbit_as_dict

# DRF serializers


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ['name']


class RabbitSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True)

    class Meta:
        model = Rabbit
        fields = ['name', 'foods']

    def update(self, instance, validated_data):
        name = validated_data.pop('name')
        if not instance.name == name:
            instance.name = name
        foods_data = validated_data.pop('foods')
        for food_data in foods_data:
            food_name = food_data.pop('name')
            food, created = Food.objects.get_or_create(name=food_name)
            if food not in instance.foods.all():
                instance.foods.add(food.pk)
        instance.save()
        return instance
