from django.contrib import admin
from .models import Enemy, Zerg, Essence, Photo

# Register your models here.

admin.site.register(Zerg)
admin.site.register(Essence)
admin.site.register(Enemy)
admin.site.register(Photo)
