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
    path('closet/<int:pk>/edit/', views.ClothingItemEdit.as_view(), name='edit_clothing_item'),
    path('closet/<int:pk>/delete/', views.ClothingItemDelete.as_view(), name='delete_clothing_item'),
    path('closet/<int:clothingitem_id>', views.clothing_items_detail, name='clothing_items_detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('outfits/', views.OutfitList.as_view(), name='outfits_index'),
    path('outfits/new', views.OutfitCreate.as_view(), name='add_outfit'),
    path('outfit_tracker/', views.outfit_tracker, name='outfit_tracker'),
]