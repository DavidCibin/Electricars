from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car
from django.views.generic.edit import CreateView

# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# # Add the Car class & list and view function below the imports
# class Car:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# cars = [
#   Car('Lolo', 'tabby', 'foul little demon', 3),
#   Car('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#   Car('Raven', 'black tripod', '3 legged car', 4)
# ]

# cars index view
def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  return render(request, 'cars/detail.html', { 'car': car })

class CarCreate(CreateView):
  model = Car
  fields = '__all__'
  success_url = '/cars/'

class CarUpdate(UpdateView):
  model = Car
  # Let's disallow the renaming of a car by excluding the name field!
  fields = ['breed', 'description', 'age']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'