from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('closet/', views.ClothingItemList.as_view(), name='clothing_items_index'),
    path('closet/tops', views.TopsList.as_view(), name='clothing_items_tops'),
    path('closet/bottoms', views.BottomsList.as_view(), name='clothing_items_bottoms'),
    path('closet/fullbody', views.FullBodyList.as_view(), name='clothing_items_fullbody'),
    path('closet/accessories', views.AccessoriesList.as_view(), name='clothing_items_accessories'),
    path('closet/shoes', views.ShoesList.as_view(), name='clothing_items_shoes'),
    path('closet/new/', views.ClothingItemCreate.as_view(), name='add_clothing_item'),
    path('closet/<int:clothingitem_id>', views.clothing_items_detail, name='clothing_items_detail'),
    path('outfits/', views.outfits_index, name='outfits_index'),
    path('outfit_tracker/', views.outfit_tracker, name='outfit_tracker'),
]