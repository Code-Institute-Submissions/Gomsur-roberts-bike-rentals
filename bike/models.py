from django.db import models
from django.contrib.auth.models import User

class Bike(models.Model):

    name = models.CharField("name", max_length=240)

    description = models.CharField("description", max_length=240)

    rental_price = models.FloatField("rental_price", default=999.99)
 
    rented_user_id =  models.IntegerField("rented_user_id")
    rental_period = models.IntegerField("rental_period", default=1)  # Default 1 day

    def __str__(self):

        return self.name


def default_profile_picture():
    return "default.png"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=240, blank=True)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default=default_profile_picture, blank=True, null=True)

    def __str__(self):
        return self.user.username