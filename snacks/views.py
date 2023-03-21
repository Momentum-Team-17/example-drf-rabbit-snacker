from django.shortcuts import render
# render generates an http response (a page the user sees)
from django.http import JsonResponse
from .models import Rabbit
from .serializers import RabbitSerializer

# Create your views here.


def list_rabbits_html(request):
    rabbits = Rabbit.objects.all()
    return render(request, 'snacks/index.html', {'rabbits': rabbits})

# this is an api endpoint style view
# generates a JSON response that's just strctured data, no HTML


def list_rabbits_json(request):
    rabbits = Rabbit.objects.all()
    data = {'rabbits': []}
    # for rabbit in rabbits:
    #     rabbit_as_dict = {
    #         'pk': rabbit.pk,
    #         'name': rabbit.name,
    #     }
    # this is serializing, putting data into a form that can be sent over a network, in this case JSON
    # we moved this to serializers.py
    for rabbit in rabbits:
        serializer = RabbitSerializer(rabbit)
        new_rabbit_dict = serializer.serialize()
        data['rabbits'].append(new_rabbit_dict)

    return JsonResponse(data)
