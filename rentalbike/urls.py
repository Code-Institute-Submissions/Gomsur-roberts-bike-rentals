from django.urls import include, path
from .views import RentalBikeCreate, RentalBikeList, RentalBikeDetail
from .views import RentalBikeUpdate, RentalBikeDelete


urlpatterns = [
	path('create/', RentalBikeCreate.as_view(), name='create-bike-rental'),
    path('', RentalBikeList.as_view()),
    path('<int:pk>/', RentalBikeDetail.as_view(), name='retrieve-bike-rental'),
    path('update/<int:pk>/', RentalBikeUpdate.as_view(), name='update-bike-rental'),
    path('delete/<int:pk>/', RentalBikeDelete.as_view(), name='delete-bike-rental')
]
