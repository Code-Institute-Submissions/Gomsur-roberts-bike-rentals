from django.urls import path
from .views import SignUpView
from django.views.generic.base import TemplateView  # new

urlpatterns = [

  path("signup/", SignUpView.as_view(), name="signup"),

  path("home", TemplateView.as_view(template_name="reserve.html"), name="home"),

]
