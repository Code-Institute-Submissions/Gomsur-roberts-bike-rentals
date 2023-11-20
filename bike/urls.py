from django.urls import include, path
from .views import BikeCreate, BikeList, BikeDetail
from .views import BikeUpdate, BikeDelete
from . import views

urlpatterns = [

    path('', views.custom, name="custom"),

    path('<int:pk>/', BikeDetail.as_view(), name='retrieve-bike'),

    path("reserve/<int:pk>/<int:user_pk>", views.reserveBike, name="reserve-bike"),

    path("return/<int:pk>/<int:user_pk>", views.returnBike, name="return-bike"),

	path('create/', BikeCreate.as_view(), name='create-bike'),

    path('update/<int:pk>/', BikeUpdate.as_view(), name='update-bike'),

    path('delete/<int:pk>/', BikeDelete.as_view(), name='delete-bike'),

]

## path("<int:question_id>/vote/", views.vote, name="vote"),

## path("about", views.about, name="about"),

## ex: /polls/5/

## path("<int:question_id>/", views.detail, name="detail"),

## ex: /polls/5/results/

## path("<int:question_id>/results/", views.results, name="results"),

## ex: /polls/5/vote/

## path("<int:question_id>/vote/", views.vote, name="vote"),

## path('', BikeList.as_view()),

## path('', login_required(direct_to_template), {'template': 'registration/login.html'}),

## path("custom", views.custom, name="custom"),

## (r'^foo/$', login_required(direct_to_template), {'template': 'foo_index.html'}),

## path('reserve/<int:pk>/<str:userid>/', BikeUpdate.as_view(), name='reserve-bike')

## path('return/<int:pk>/', BikeUpdate.as_view(), name='return-bike'),
