from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import ClothingItem
# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def clothing_items_index(request):
  return render(request, 'my_closet.html')

class ClothingItemCreate(CreateView):
  model = ClothingItem
  fields = '__all__'

def outfits_index(request):
  return render(request, 'outfits.html')

def outfit_tracker(request):
  return render(request, 'outfit_tracker.html')