from django.contrib import admin
from .models import User, Rabbit, Food
# Register your models here.
admin.site.register(User)
admin.site.register(Rabbit)
admin.site.register(Food)
