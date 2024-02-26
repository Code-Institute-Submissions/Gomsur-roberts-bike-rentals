from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.shortcuts import redirect

class SignUpView(generic.CreateView):

    form_class = UserCreationForm

    success_url = reverse_lazy("login")

    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


def logout_view(request):
    logout(request)
    return redirect('/')