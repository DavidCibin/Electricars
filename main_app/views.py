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
from .forms import ProfileForm


# Create your views here.

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
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
      user.username = user.email
      user.profile.first_name = form.cleaned_data.get('first_name')
      user.profile.last_name = form.cleaned_data.get('last_name')
      user.profile.email = form.cleaned_data.get('email')
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

# cars index view ##################################################
def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

# cars details view ##################################################
def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  profile_form = ProfileForm()
  booking_form = BookingForm()
  
  return render(request, 'cars/detail.html', { 'car': car, 'booking_form': booking_form, 'profile_form': profile_form })


def addbooking(request, car_id): 
  if request.method == 'POST':
    
    profile_form = ProfileForm(request.POST)
    booking_form = BookingForm(request.POST)
    print(request.POST)
    if booking_form.is_valid() or profile_form.is_valid(): 
      # do stuff here
      # form = ProfileForm(request.POST)
        new_profile = profile_form.save(commit=False)
        new_profile.car_id = car_id
        new_profile.user_id = request.user.id
        new_profile.save()
      # do stuff here
      # form = BookingForm(request.POST)
        new_booking = booking_form.save(commit=False)
        new_booking.car_id = car_id
        new_booking.user_id = request.user.id
        new_booking.save()
    return redirect('detail', car_id=car_id)
  
  else:
    profile_form = ProfileForm(prefix="profile_form")
    booking_form = BookingForm(prefix="booking_form")



# def add_profile(request, car_id):
#   # create a ModelForm instance using the data in request.POST
#   form = ProfileForm(request.POST)
#   # validate the form
#   if form.is_valid():
#     # don't save the form to the db until it
#     # has the car_id assigned
#     new_profile = form.save(commit=False)
#     new_profile.car_id = car_id
#     new_profile.save()
#   return redirect('detail', car_id=car_id)

# def add_booking(request, car_id):
#   # create a ModelForm instance using the data in request.POST
#   form = BookingForm(request.POST)
#   # validate the form
#   if form.is_valid():
#     # don't save the form to the db until it
#     # has the car_id assigned
#     new_booking = form.save(commit=False)
#     new_booking.car_id = car_id
#     new_booking.user_id = request.user.id
#     new_booking.save()
#   return redirect('detail', car_id=car_id)
class CarCreate(CreateView):
  model = Car
  fields = ['make', 'model', 'passengers', 'luggage', 'erange', 'price']
  
  # This inherited method is called when a
  # valid lizard form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the lizard
    # Let the CreateView do its job as usual
    return super().form_valid(form)

# class CarCreate(CreateView):
#   model = Car
#   fields = '__all__'
#   success_url = '/cars/'

class CarUpdate(UpdateView):
  model = Car
  # Let's disallow the renaming of a car by excluding the name field!
  fields = '__all__'

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'

class ProfileUpdate(UpdateView):
  model = Profile
  # Let's disallow the renaming of a car by excluding the name field!
  fields = ['address1', 'address2', 'city', 'state', 'zipcode', ]
  success_url = '/accounts/'

# def cars_index(request):
#   return render(request, 'cars/index.html', { 'cars': cars })

def account(request):
  # car = User.objects.get(user=user)
  profile = Profile.objects.all()
  return render(request, 'accounts/profile.html', { 'profile': profile })

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')