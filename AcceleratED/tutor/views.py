from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, imageUpload, tutorPersonalform, tutorEduform, tutorWorkform, tutorQAform
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Tutor
from django.shortcuts import render, redirect
from django.core.mail import message, send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages


# Create your views here.

User = get_user_model()

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
            if request.user.is_superuser:
                return redirect('index')
            return redirect('profile')
    else:
        # Create an empty instance of Django's AuthenticationForm to generate the necessary html on the template.
        form = AuthenticationForm()
    return render(request, 'tutor/index.html', {'form': form})


def register_view(request):
    # This function renders the registration form page and create a new user based on the form data
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        # check whether it's valid: for example it verifies that password1 and password2 match
        if form.is_valid():
            newUser =form.save(commit=False)
            newUser.is_active =False
            newUser.save()
            mail_subject ='Activate your account'
            message = render_to_string('tutor/password/activate.html', {
                'user':newUser,
                'domain': get_current_site(request).domain,
                "uid": urlsafe_base64_encode(force_bytes(newUser.pk)),
                'token': default_token_generator.make_token(newUser),
                'protocol': 'http',
            })
            send_mail(mail_subject, message, 'admin@example.com', [newUser.email], fail_silently=False)
            
            return HttpResponse('Check your email and follow the link to activate your account')
    else:
        # Create an empty instance of UserRegistrationForm to generate the necessary html on the template.
        form = UserRegistrationForm()
    return render(request, 'tutor/register.html', {'form': form})  


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('profile')
    else:
        return HttpResponse('Activation link is invalid!')

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "tutor/password/password_reset_email.txt"
					c = {
					"email":user.email,
                    'domain': get_current_site(request).domain,
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ('password_reset_done')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="tutor/password/password_reset.html", context={"password_reset_form":password_reset_form})

@login_required(login_url='login')
def edit_view(request):
    return render(request, 'tutor/edit.html', {'authenticated': True})


@login_required(login_url='login')
def profile_view(request):
    User = get_user_model()
    user = User.objects.get(email=request.user.email)
    tutor = Tutor.objects.filter(email=user)
    return render(request, 'tutor/profile.html', {'authenticated': True, "Tutor": tutor, "User": user})
@login_required(login_url='login')
def del_account(request):
    User = get_user_model()
    current =User.objects.get(id=request.user.id)
    current.tutor.resume.delete()
    current.tutor.image.delete()
    current.delete()
    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def edit_personal_view(request):
    profiles = Tutor.objects.get(email_id=request.user.id)
    form = tutorPersonalform(request.POST or None, instance=profiles)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'tutor/personal.html', {'authenticated': True, 'form': form})
    
@login_required(login_url='login')    
def edit_edu_view(request):
    profiles = Tutor.objects.get(email_id=request.user.id)
    form = tutorEduform(request.POST or None, instance=profiles)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'tutor/edu.html', {'authenticated': True, 'form': form})


@login_required(login_url='login')
def edit_work_view(request):
    profiles = Tutor.objects.get(email_id=request.user.id)
    form = tutorWorkform(request.POST or None, instance=profiles)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'tutor/work.html', {'authenticated': True, 'form': form})


@login_required(login_url='login')
def edit_qa_view(request):
    profiles = Tutor.objects.get(email_id=request.user.id)
    form = tutorQAform(request.POST or None, instance=profiles)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'tutor/qa.html', {'authenticated': True, 'form': form})


@login_required(login_url='login')
def imgUpload_view(request):
    profiles = Tutor.objects.get(email_id=request.user.id)
    form = imageUpload(request.POST or None, request.FILES or None, instance=profiles)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'tutor/imgUpload.html', {'authenticated': True, 'form': form})
