from django.shortcuts import render

from rest_framework import generics

from django.http import HttpResponse
from django.template import loader

## https://docs.djangoproject.com/en/4.2/intro/tutorial03/

def home(request):

    print("home home")

    template = loader.get_template("index.html")

    context = {
        "latest_question_list": "yo",
    }

    return HttpResponse(template.render(context, request))

def about(request):

    print("about about")

    template = loader.get_template("about.html")

    context = {
        "latest_question_list": "yo",
    }

    return HttpResponse(template.render(context, request))

def accessories(request):

    print("accessories accessories accessories")

    template = loader.get_template("accessories.html")

    context = {
        "latest_question_list": "yo",
    }

    return HttpResponse(template.render(context, request))
