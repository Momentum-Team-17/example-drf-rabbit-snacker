from .models import Rabbit


class RabbitSerializer():
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
