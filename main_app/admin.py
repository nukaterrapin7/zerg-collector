from django.contrib import admin
from .models import Enemy, Zerg, Essence

# Register your models here.

admin.site.register(Zerg)
admin.site.register(Essence)
admin.site.register(Enemy)
