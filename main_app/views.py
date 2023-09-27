from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClothingItem, Outfit
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

class ClothingItemList(LoginRequiredMixin, ListView):
  def get_queryset(self):
    queryset = ClothingItem.objects.filter(user=self.request.user)
    return queryset

class TopsList(LoginRequiredMixin, ListView):
  def get_queryset(self):
    queryset = ClothingItem.objects.filter(category='T', user=self.request.user)
    return queryset

class BottomsList(LoginRequiredMixin, ListView):
  def get_queryset(self):
    queryset = ClothingItem.objects.filter(category='B', user=self.request.user)
    return queryset

class FullBodyList(LoginRequiredMixin, ListView):
  def get_queryset(self):
    queryset = ClothingItem.objects.filter(category='F', user=self.request.user)
    return queryset

class AccessoriesList(LoginRequiredMixin, ListView):
  def get_queryset(self):
    queryset = ClothingItem.objects.filter(category='A', user=self.request.user)
    return queryset

class ShoesList(LoginRequiredMixin, ListView):
  def get_queryset(self):
    queryset = ClothingItem.objects.filter(category='S', user=self.request.user)
    return queryset

class ClothingItemCreate(LoginRequiredMixin, CreateView):
  model= ClothingItem
  fields = ['description', 'category', 'colors', 'date_acquired', 'place_purchased', 'price', 'size', 'tags']
  success_url = '/closet'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ClothingItemEdit(LoginRequiredMixin, UpdateView):
  model = ClothingItem
  fields = ['description', 'category', 'colors', 'date_acquired', 'place_purchased', 'price', 'size', 'tags']

class ClothingItemDelete(LoginRequiredMixin, DeleteView):
  model = ClothingItem
  fields = '__all__'
  success_url = '/closet'

@login_required
def clothing_items_detail(request, clothingitem_id):
  clothingitem = ClothingItem.objects.get(id=clothingitem_id)
  return render(request, 'clothing_item_detail.html', {'clothingitem': clothingitem})

class OutfitList(LoginRequiredMixin, ListView):
  def get_queryset(self):
    queryset = Outfit.objects.filter(user=self.request.user)
    return queryset

class OutfitCreate(LoginRequiredMixin, CreateView):
  model = Outfit
  fields = ['description', 'clothing_items']
  success_url = '/outfits'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

@login_required
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
