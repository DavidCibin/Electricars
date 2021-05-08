from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Car, Photo, Profile
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

from .forms import BookingForm


# Create your views here.

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'electricar'
def add_photo(request, car_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to car_id or car (if you have a car object)
      photo = Photo(url=url, car_id=car_id)
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('detail', car_id=car_id)

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = SignUpForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      user.refresh_from_db()
      # user.profile.first_name = form.cleaned_data.get('first_name')
      # user.profile.last_name = form.cleaned_data.get('last_name')
      # user.profile.email = form.cleaned_data.get('email')
      user.profile.bio = form.cleaned_data.get('bio')
      user.save()
      # username = form.cleaned_data.get('username')
      # password = form.cleaned_data.get('password1')
      # user = authenticate(username=username, password=password)
      login(request, user)
      # This is how we log a user in via code
      # login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = SignUpForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# cars index view
def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  booking_form = BookingForm()
  return render(request, 'cars/detail.html', { 'car': car, 'booking_form': booking_form })

def add_booking(request, car_id):
  # create a ModelForm instance using the data in request.POST
  form = BookingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the car_id assigned
    new_booking = form.save(commit=False)
    new_booking.car_id = car_id
    new_booking.save()
  return redirect('detail', car_id=car_id)

class CarCreate(CreateView):
  model = Car
  fields = '__all__'
  success_url = '/cars/'

class CarUpdate(UpdateView):
  model = Car
  # Let's disallow the renaming of a car by excluding the name field!
  fields = '__all__'

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'

def account(request):
  # car = User.objects.get(user=user)
  return render(request, 'accounts/profile.html')