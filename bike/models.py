from django.db import models

class Bike(models.Model):

    name = models.CharField("name", max_length=240)

    description = models.CharField("description", max_length=240)

    rental_price = models.FloatField("rental_price", default=999.99)
 
    rented_user_id =  models.IntegerField("rented_user_id")

    def __str__(self):

        return self.name
