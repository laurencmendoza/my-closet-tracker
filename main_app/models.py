from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
CATEGORIES = [
    ("T", "Tops"), 
    ("B", "Bottoms"), 
    ("F", "Full Body"),
    ("A", "Accessories"),
    ("S", "Shoes"),
]


class Color(models.Model):
    color=models.CharField(max_length=30)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.color


class Tag(models.Model):
    tag=models.CharField(max_length=30)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag


class ClothingItem(models.Model):
    description= models.CharField(max_length=100)
    category= models.CharField(max_length=1, choices=CATEGORIES, default=CATEGORIES[0][0])
    colors=models.ManyToManyField(Color)
    date_acquired= models.DateField()
    place_purchased= models.CharField(max_length=100)
    price= models.DecimalField(decimal_places=2, max_digits=10)
    size= models.CharField(max_length=4)
    tags=models.ManyToManyField(Tag)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('clothing_items_detail', kwargs={'clothingitem_id': self.id})


class Outfit(models.Model):
    description= models.CharField(max_length=100)
    clothing_items=models.ManyToManyField(ClothingItem)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Photo(models.Model):
    url = models.CharField(max_length=200)
    clothingitem = models.ForeignKey(ClothingItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.url