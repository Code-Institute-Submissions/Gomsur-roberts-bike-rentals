from django.shortcuts import render
from .models import Bike, Profile
from rest_framework import generics
from .serializers import BikeSerializer
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import reverse
from django.db import IntegrityError
from .forms import ProfileForm
# https://docs.djangoproject.com/en/4.2/intro/tutorial03/


# user = User(username=new_data['username'], email=new_data['email'],
# first_name=new_data['email'])
# user.save()
# user_id = user.id

@login_required
def profile_view(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    bike_rentals = Bike.objects.filter(rented_user_id=user.id)
    context = {
        'user': user,
        'profile': profile,
        'bike_rentals': bike_rentals
    }
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    
    context = {
        'form': form
    }
    return render(request, 'edit_profile.html', context)

@login_required
def reserveBike(request, pk, user_pk):
    t = Bike.objects.get(id=pk)
    t.rented_user_id = user_pk  # Change rented_user_id to the user who reserves the bike
    t.rental_period = 1  # Reset rental period to default (1 day)
    t.save()

    # Get all bikes for display in the template
    latest_question_list = Bike.objects.all()

    # Prepare context data for the template
    context = {
       "latest_question_list": latest_question_list,
       "status_message": f"You have successfully reserved the {t.name}.",
    }

    # Decide which template to render based on user's role
    if request.user.is_superuser:
        template_name = "manage.html"
    else:
        template_name = "reserve.html"

    # Render the template with the context data
    template = loader.get_template(template_name)
    return HttpResponse(template.render(context, request))


@login_required
def cancel_rental_view(request, rental_id):
    rental = get_object_or_404(Bike, pk=rental_id)
    
    if request.method == 'POST':
        # Handle form submission
        rented_user_id = request.POST.get('rented_user_id', None)
        if rented_user_id is None:
            rental.rented_user_id = 0
            rental.rental_period = 1  # Reset rental period to 1
        else:
            rental.rented_user_id = int(rented_user_id)
        
        rental.save()
        
        return redirect('profile')
    
    context = {'rental': rental}
    return render(request, 'cancel_rental.html', context)

@login_required
def extend_rental_view(request, rental_id):
    rental = get_object_or_404(Bike, pk=rental_id)

    if request.method == 'POST':
        # Update the rental period
        new_rental_period = request.POST.get('new_rental_period')
        if new_rental_period is not None and new_rental_period != '':
            rental.rental_period = int(new_rental_period)
            rental.save()
            return redirect('profile')
        else:
            # Handle case where no new rental period was provided
            context = {'rental': rental, 'error_message': 'Please enter a valid rental period.'}
            return render(request, 'extend_rental.html', context)

    context = {'rental': rental}
    return render(request, 'extend_rental.html', context)



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


'''
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

    # return HttpResponse(template.render(context, request))

    latest_question_list = Bike.objects.all()

    template = loader.get_template("reserve.html")

    context = {
       "latest_question_list": latest_question_list,
       "status_message": ("You have successfull reserved the %s." % t.name),
    }

    return HttpResponse(template.render(context, request))
'''
    
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
 