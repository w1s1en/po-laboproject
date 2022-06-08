from django.contrib import admin

from zawody.models import Bike, Competition, Player

admin.site.register(Competition)
admin.site.register(Player)
admin.site.register(Bike)
# Register your models here.
