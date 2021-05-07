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
    return self.make
    
  # Add this method
  def get_absolute_url(self):
    return reverse('detail', kwargs={'car_id': self.id})

class Photo(models.Model):
  url = models.CharField(max_length=200)
  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for car_id: {self.car_id} @{self.url}"


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    bio = models.CharField(max_length=100, help_text='bio')

class Meta:
        managed = False
        db_table = 'profile' 

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:     
        Profile.objects.create(user=instance)
    instance.profile.save()        