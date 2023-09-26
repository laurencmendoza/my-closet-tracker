from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import ClothingItem
# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

class ClothingItemList(ListView):
  model = ClothingItem

class ClothingItemCreate(CreateView):
  model = ClothingItem
  fields = '__all__'
  success_url = '/closet'

def clothing_items_detail(request, clothingitem_id):
  clothingitem = ClothingItem.objects.get(id=clothingitem_id)
  return render(request, 'clothing_item_detail.html', {'clothingitem': clothingitem})

def outfits_index(request):
  return render(request, 'outfits.html')

def outfit_tracker(request):
  return render(request, 'outfit_tracker.html')