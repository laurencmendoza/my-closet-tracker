from django.contrib import admin
# import your models here
from .models import ClothingItem, Color

# Register your models here.
admin.site.register(ClothingItem)
admin.site.register(Color)