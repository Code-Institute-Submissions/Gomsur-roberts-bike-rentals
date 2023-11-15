from rest_framework import serializers
from .models import RentalBike
 
class RentalBikeSerializer(serializers.ModelSerializer):

    class Meta:

        model = RentalBike 

        fields = ['pk', 'name', 'email', 'created']
