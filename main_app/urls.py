from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('closet/', views.ClothingItemList.as_view(), name='clothing_items_index'),
    path('closet/new/', views.ClothingItemCreate.as_view(), name='add_clothing_item'),
    path('closet/<int:clothingitem_id>', views.clothing_items_detail, name='clothing_items_detail'),
    path('outfits/', views.outfits_index, name='outfits_index'),
    path('outfit_tracker/', views.outfit_tracker, name='outfit_tracker'),
]