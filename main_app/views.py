import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClothingItem, Outfit, Photo, OutfitPhoto, Color, Tag
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
  fields = ['description', 'category', 'date_acquired', 'place_purchased', 'price', 'size']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class ClothingItemEdit(LoginRequiredMixin, UpdateView):
  model = ClothingItem
  fields = ['description', 'category', 'date_acquired', 'place_purchased', 'price', 'size']


class OutfitEdit(LoginRequiredMixin, UpdateView):
  model = Outfit
  fields = ['description']


class ClothingItemDelete(LoginRequiredMixin, DeleteView):
  model = ClothingItem
  fields = '__all__'
  success_url = '/closet'


class OutfitDelete(LoginRequiredMixin, DeleteView):
  model = Outfit
  fields = '__all__'
  success_url = '/outfits'


@login_required
def clothing_items_detail(request, clothingitem_id):
  clothingitem = ClothingItem.objects.get(id=clothingitem_id)
  color_id_list = clothingitem.colors.all().values_list('id')
  tag_id_list = clothingitem.tags.all().values_list('id')
  usercolors = Color.objects.filter(user=request.user)
  colors_clothingitem_doesnt_have = usercolors.exclude(id__in=color_id_list)
  usertags = Tag.objects.filter(user=request.user)
  tags_clothingitem_doesnt_have = usertags.exclude(id__in=tag_id_list)
  return render(request, 'clothing_item_detail.html', {'clothingitem': clothingitem, 'colors': colors_clothingitem_doesnt_have, 'tags': tags_clothingitem_doesnt_have})


class OutfitList(LoginRequiredMixin, ListView):
  def get_queryset(self):
    queryset = Outfit.objects.filter(user=self.request.user)
    return queryset


class OutfitCreate(LoginRequiredMixin, CreateView):
  model = Outfit
  fields = ['description']
  success_url = '/outfits'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


@login_required
def outfit_detail(request, outfit_id):
  outfit = Outfit.objects.get(id=outfit_id)
  clothingitem_id_list = outfit.clothing_items.all().values_list('id')
  userclothingitems = ClothingItem.objects.filter(user=request.user)
  clothingitems_outfit_doesnt_have = userclothingitems.exclude(id__in=clothingitem_id_list)
  return render(request, 'outfit_detail.html', {'outfit': outfit, 'clothingitems':clothingitems_outfit_doesnt_have})


@login_required
def outfit_tracker(request):
  return render(request, 'outfit_tracker.html')


@login_required
def assoc_color(request, clothingitem_id, color_id):
  ClothingItem.objects.get(id=clothingitem_id).colors.add(color_id)
  return redirect('clothing_items_detail', clothingitem_id=clothingitem_id)


@login_required
def unassoc_color(request, clothingitem_id, color_id):
  ClothingItem.objects.get(id=clothingitem_id).colors.remove(color_id)
  return redirect('clothing_items_detail', clothingitem_id=clothingitem_id)


@login_required
def assoc_tag(request, clothingitem_id, tag_id):
  ClothingItem.objects.get(id=clothingitem_id).tags.add(tag_id)
  return redirect('clothing_items_detail', clothingitem_id=clothingitem_id)


@login_required
def unassoc_tag(request, clothingitem_id, tag_id):
  ClothingItem.objects.get(id=clothingitem_id).tags.remove(tag_id)
  return redirect('clothing_items_detail', clothingitem_id=clothingitem_id)


@login_required
def assoc_clothingitem(request, outfit_id, clothingitem_id):
  Outfit.objects.get(id=outfit_id).clothing_items.add(clothingitem_id)
  return redirect('outfits_detail', outfit_id=outfit_id)

@login_required
def unassoc_clothingitem(request, outfit_id, clothingitem_id):
  Outfit.objects.get(id=outfit_id).clothing_items.remove(clothingitem_id)
  return redirect('outfits_detail', outfit_id=outfit_id)


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


def add_clothing_item_photo(request, clothingitem_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
      s3 = boto3.client('s3')
      # need a unique "key" for S3 / needs image file extension too
      key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
      # just in case something goes wrong
      try:
          bucket = os.environ['S3_BUCKET']
          s3.upload_fileobj(photo_file, bucket, key)
          # build the full url string
          url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
          # we can assign to cat_id or cat (if you have a cat object)
          Photo.objects.create(url=url, clothingitem_id=clothingitem_id)
      except Exception as e:
          print('An error occurred uploading file to S3')
          print(e)
  return redirect('clothing_items_detail', clothingitem_id=clothingitem_id)


def add_outfit_photo(request, outfit_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
      s3 = boto3.client('s3')
      # need a unique "key" for S3 / needs image file extension too
      key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
      # just in case something goes wrong
      try:
          bucket = os.environ['S3_BUCKET']
          s3.upload_fileobj(photo_file, bucket, key)
          # build the full url string
          url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
          # we can assign to cat_id or cat (if you have a cat object)
          OutfitPhoto.objects.create(url=url, outfit_id=outfit_id)
      except Exception as e:
          print('An error occurred uploading file to S3')
          print(e)
  return redirect('outfits_detail', outfit_id=outfit_id)