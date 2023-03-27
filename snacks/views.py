from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
# render generates an http response (a page the user sees)
from django.http import JsonResponse
from .models import Food, Rabbit
from .serializers import RabbitSerializer, RabbitDIYSerializer, FoodSerializer


# HTML homepage view
def list_rabbits_html(request):
    rabbits = Rabbit.objects.all()
    return render(request, 'snacks/index.html', {'rabbits': rabbits})

# this is a non-DRF api endpoint view
# generates a JSON response that's just structured data, no HTML


def list_rabbits_json(request):
    rabbits = Rabbit.objects.all()
    data = {'rabbits': []}
    for rabbit in rabbits:
        serializer = RabbitDIYSerializer(rabbit)
        new_rabbit_dict = serializer.serialize()
        data['rabbits'].append(new_rabbit_dict)

    return JsonResponse(data)

# DRF API endpoint


class RabbitDetail(generics.RetrieveUpdateAPIView):
    serializer_class = RabbitSerializer
    queryset = Rabbit.objects.all()
    permission_classes = [IsAuthenticated]
