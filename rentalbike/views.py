from django.shortcuts import render
from .models import RentalBike
from rest_framework import generics
from .serializers import RentalBikeSerializer


class RentalBikeCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
	queryset = RentalBike.objects.all(),
	serializer_class = RentalBikeSerializer


class RentalBikeList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = RentalBike.objects.all()
    serializer_class = RentalBikeSerializer


class RentalBikeDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = RentalBike.objects.all()
    serializer_class = RentalBikeSerializer


class RentalBikeUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = RentalBike.objects.all()
    serializer_class = RentalBikeSerializer


class RentalBikeDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = RentalBike.objects.all()
    serializer_class = RentalBikeSerializer
