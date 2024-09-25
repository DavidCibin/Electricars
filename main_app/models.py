from django.db import models
from django.db.models.fields import EmailField
from django.urls import reverse
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Car(models.Model):
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  passengers = models.IntegerField()
  luggage = models.IntegerField()
  suitcase = models.IntegerField()
  erange = models.IntegerField()
  price = models.DecimalField(max_digits=6, decimal_places=2)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.make}/{self.model} (car id# {self.id})"
    
  # Add this method
  def get_absolute_url(self):
    return reverse('detail', kwargs={'car_id': self.id})

class Photo(models.Model):
  url = models.CharField(max_length=200)
  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo: {self.car.make}/{self.car.model} (car id# {self.car_id})"


INSURANCE = (
    ('N', 'No Coverage'),
    ('F', 'Full Coverage (+$20.00/day)'),
)

class Booking(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  car = models.ForeignKey(Car, on_delete=models.CASCADE)
  start_date = models.DateField()
  end_date = models.DateField()
  total = models.DecimalField(max_digits=6, decimal_places=2)
  insurance = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=INSURANCE,
    # set the default value for meal to be 'B'
    default=INSURANCE[0][0]
  )

  def get_absolute_url(self):
    return reverse('booking', kwargs={'booking_id': self.id})

  class Meta:
    ordering = ['start_date']

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"Reservation: rEs{self.id}"


class Profile(models.Model):
    # # admin view only???
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    phone = PhoneField(blank=True)
    address1 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
      # Nice method for obtaining the friendly value of a Field.choice
      return f"ID#:{self.user.id} - {self.user.first_name} {self.user.last_name}"

class Meta:
        managed = False
        db_table = 'profile' 

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:     
        Profile.objects.create(user=instance)
    instance.profile.save()        

class Contact(models.Model):
  name = models.CharField(max_length=100)
  email = EmailField()
  subject = models.CharField(max_length=254)
  message = models.TextField(max_length=100)
  
  def __str__(self):
      return self.name