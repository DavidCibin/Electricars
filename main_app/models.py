from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Car(models.Model):
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  passengers = models.IntegerField()
  luggage = models.IntegerField()
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
    ('F', 'Full Coverage'),
)

class Booking(models.Model):
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

  # how to get the booking id??????????
  def get_absolute_url(self):
    return reverse('booking', kwargs={'booking_id': self.booking.id})


  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_insurance_display()} P/U {self.start_date} - D/O {self.start_date}"


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # admin view
    bio = models.CharField(max_length=100, help_text='bbbbio')
    Address1 = models.CharField(max_length=100, help_text='Address 1')
    Address2 = models.CharField(max_length=100, help_text='Address 2')
    city = models.CharField(max_length=100, help_text='city')
    state = models.CharField(max_length=2, help_text='state')
    zipcode = models.CharField(max_length=5, help_text='zipcode')

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