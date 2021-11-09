from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, tutorIntakeform
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Tutor
from django.shortcuts import get_object_or_404



# Create your views here.

def login_view(request):
    # this function authenticates the user based on username and password
    # AuthenticationForm is a form for logging a user in.
    # if the request method is a post
    if request.method == 'POST':
        # Plug the request.post in AuthenticationForm
        form = AuthenticationForm(data=request.POST)
        # check whether it's valid:
        if form.is_valid():
            # get the user info from the form data and login the user
            user = form.get_user()
            login(request, user)
            # redirect the user to index page
            return redirect('profile')
    else:
        # Create an empty instance of Django's AuthenticationForm to generate the necessary html on the template.
        form = AuthenticationForm()
    return render(request, 'tutor/index.html', {'form': form})


def register_view(request):
    # This function renders the registration form page and create a new user based on the form data
    if request.method == 'POST':
        # We use Django's UserCreationForm which is a model created by Django to create a new user.
        # UserCreationForm has three fields by default: username (from the user model), password1, and password2.
        # If you want to include email as well, switch to our own custom form called UserRegistrationForm
        form = UserRegistrationForm(request.POST)
        # check whether it's valid: for example it verifies that password1 and password2 match
        if form.is_valid():
            form.save()
            # User = get_user_model()
            # new_Tutor = Tutor(email=User)
            # new_Tutor.save()
            # if you want to login the user directly after saving, use the following two lines instead, and redirect to index
            # user = form.save()
            # login(user)
            # redirect the user to login page so that after registration the user can enter the credentials
            return redirect('login')
    else:
        # Create an empty instance of Django's UserCreationForm to generate the necessary html on the template.
        form = UserRegistrationForm()
    return render(request, 'tutor/register.html', {'form': form})


@login_required(login_url='login')
def edit_view(request):
    # User = get_user_model()
    # profile = User.objects.get(pk=Tutor.email)
    # profile = Tutor.objects.select_related()
    profiles = Tutor.objects.get(email_id=request.user.id)
    # profile =User.objects.exclude(pk__in=profiles)

    
    form = tutorIntakeform(request.POST or None, instance=profiles)
    if form.is_valid():
            form.save()
            # User = get_user_model()
            # media.owner = str(User.objects.get(email=request.user.email))
            # media.save()
            return redirect('profile')
    else:
        form = tutorIntakeform()
        # User = get_user_model()
        # user = User.objects.get(email=request.user.email)
    return render(request, 'tutor/edit.html', { 'authenticated': True, 'form': form })


@login_required(login_url='login')
def profile_view(request):
    User = get_user_model()
    user = User.objects.get(email=request.user.email)
    tutor = Tutor.objects.filter(email=user)
    return render(request, 'tutor/profile.html', {'authenticated': True, "Tutor": tutor})

def del_account(request):
    User = get_user_model()
    current =User.objects.get(id=request.user.id)
    current.delete()
    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')

