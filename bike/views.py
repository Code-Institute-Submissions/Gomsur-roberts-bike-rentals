from django.shortcuts import render
from .models import Bike
from rest_framework import generics
from .serializers import BikeSerializer
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect
from django.shortcuts import reverse
# https://docs.djangoproject.com/en/4.2/intro/tutorial03/


# user = User(username=new_data['username'], email=new_data['email'],
# first_name=new_data['email'])
# user.save()
# user_id = user.id


class BikeCreate(generics.CreateAPIView):

    queryset = Bike.objects.all(),

    serializer_class = BikeSerializer

    class BikeList(generics.ListAPIView):

        queryset = Bike.objects.all()

        serializer_class = BikeSerializer

    class BikeDetail(generics.RetrieveAPIView):

        queryset = Bike.objects.all()

        serializer_class = BikeSerializer

    class BikeUpdate(generics.RetrieveUpdateAPIView):

        queryset = Bike.objects.all()

        serializer_class = BikeSerializer

    class BikeDelete(generics.RetrieveDestroyAPIView):

        queryset = Bike.objects.all()

        serializer_class = BikeSerializer

    def detail(request, question_id):
        return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

    def reserveBike(request, pk, user_pk):

        t = Bike.objects.get(id=pk)

    t.rented_user_id = user_pk  # change field

    t.save()  # this will update only

    ##

    latest_question_list = Bike.objects.all()

    context = {
       "latest_question_list": latest_question_list,
      "status_message": ("You have successfull reserved the %s." % t.name),
    }

    if request.user.is_superuser:

        template = loader.get_template("manage.html")

    else:

        template = loader.get_template("reserve.html")

    return HttpResponse(template.render(context, request))

    latest_question_list = Bike.objects.all()

    template = loader.get_template("reserve.html")

    context = {
       "latest_question_list": latest_question_list,
      "status_message": ("You have successfull reserved the %s." % t.name),
    }

    return HttpResponse(template.render(context, request))

    def returnBike(request, pk, user_pk):

        t = Bike.objects.get(id=pk)

    t.rented_user_id = 0  # change field

    t.save()  # this will update only

    ##

    latest_question_list = Bike.objects.all()

    context = {
       "latest_question_list": latest_question_list,
       "status_message": ("You have successfull returned the %s." % t.name),
    }

    if request.user.is_superuser:

        template = loader.get_template("manage.html")

    else:

        template = loader.get_template("reserve.html")

    return HttpResponse(template.render(context, request))

    @login_required
def custom(request):
    print("custom custom custom")

    latest_question_list = Bike.objects.all()

    context = {

        "latest_question_list": latest_question_list,
    }

    if request.user.is_superuser:

        template = loader.get_template("manage.html")

    else:

        template = loader.get_template("reserve.html")

    return HttpResponse(template.render(context, request))

    def about(request):

        print("aboutpage aboutpage aboutpage")

    template = loader.get_template("about.html")

    context = {

        "latest_question_list": "yo",

    }

    return HttpResponse(template.render(context, request))
 