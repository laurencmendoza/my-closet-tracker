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

def outfits_index(request):
  return render(request, 'outfits.html')

def outfit_tracker(request):
  return render(request, 'outfit_tracker.html')