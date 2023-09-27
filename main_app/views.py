from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClothingItem, Outfit
# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

class ClothingItemList(ListView):
  model = ClothingItem

class TopsList(ListView):
  def get_queryset(self):
    queryset = ClothingItem.objects.filter(category='T')
    return queryset

class BottomsList(ListView):
  def get_queryset(self):
    queryset = ClothingItem.objects.filter(category='B')
    return queryset

class FullBodyList(ListView):
  def get_queryset(self):
    queryset = ClothingItem.objects.filter(category='F')
    return queryset

class AccessoriesList(ListView):
  def get_queryset(self):
    queryset = ClothingItem.objects.filter(category='A')
    return queryset

class ShoesList(ListView):
  def get_queryset(self):
    queryset = ClothingItem.objects.filter(category='S')
    return queryset
  
class ClothingItemCreate(CreateView):
  model = ClothingItem
  fields = '__all__'
  success_url = '/closet'

class ClothingItemEdit(UpdateView):
  model = ClothingItem
  fields = '__all__'

class ClothingItemDelete(DeleteView):
  model = ClothingItem
  fields = '__all__'
  success_url = '/closet'

def clothing_items_detail(request, clothingitem_id):
  clothingitem = ClothingItem.objects.get(id=clothingitem_id)
  return render(request, 'clothing_item_detail.html', {'clothingitem': clothingitem})

class OutfitList(ListView):
  model = Outfit

class OutfitCreate(CreateView):
  model = Outfit
  fields = '__all__'
  success_url = '/outfits'

def outfit_tracker(request):
  return render(request, 'outfit_tracker.html')