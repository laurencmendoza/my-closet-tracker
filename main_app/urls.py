from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('closet/', views.clothing_items_index, name='clothing_items_index'),
    path('closet/new/', views.add_clothing_item, name='add_clothing_item'),
    path('outfits/', views.outfits_index, name='outfits_index'),
    path('outfit_tracker/', views.outfit_tracker, name='outfit_tracker'),
]