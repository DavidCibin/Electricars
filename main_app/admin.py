from django.contrib import admin
from .models import Car, Photo, Profile, Booking
# import your models here

# Register your models here
admin.site.register(Car)
admin.site.register(Photo)
admin.site.register(Profile)
admin.site.register(Booking)