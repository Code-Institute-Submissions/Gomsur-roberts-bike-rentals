from django.contrib import admin
from .models import Bike, Profile

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'rental_price', 'rented_user_id', 'rental_period']
    list_filter = ['rented_user_id']
    search_fields = ['name', 'description', 'rented_user_id']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'bio', 'birth_date', 'phone_number', 'address', 'city', 'state', 'zip_code']
    search_fields = ['user__username', 'full_name', 'phone_number', 'address', 'city', 'state', 'zip_code']
