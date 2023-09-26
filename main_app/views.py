from django.shortcuts import render

# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def clothing_items_index(request):
  return render(request, 'my_closet.html')

def add_clothing_item(request):
  return render(request, 'add_clothing_item.html')

def outfits_index(request):
  return render(request, 'outfits.html')

def outfit_tracker(request):
  return render(request, 'outfit_tracker.html')