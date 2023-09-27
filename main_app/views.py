from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClothingItem, Outfit
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

class ClothingItemList(ListView):
  def get_queryset(self):
    queryset = ClothingItem.objects.filter(user=self.request.user)
    return queryset

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
  fields = ['description', 'category', 'colors', 'date_acquired', 'place_purchased', 'price', 'size', 'tags']
  success_url = '/closet'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
