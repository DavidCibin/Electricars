from django.contrib import admin
from .models import Car, Contact, Photo, Profile, Booking, Contact
# import your models here

# Register your models here
admin.site.register(Car)
admin.site.register(Photo)
admin.site.register(Profile)
admin.site.register(Booking)
admin.site.register(Contact)