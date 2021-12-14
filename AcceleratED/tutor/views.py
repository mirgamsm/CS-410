# Tutor views
# View functions take web requests and return web responses
from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, imageUpload, tutorPersonalform, tutorEduform, tutorWorkform, tutorQAform
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Tutor
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site

"""Set User to Abstract Model"""
User = get_user_model()


"""Controller for initial login page of the app"""
def login_view(request):
    if request.method == 'POST':
        # Plug the request.post in AuthenticationForm
        form = AuthenticationForm(data=request.POST)
        # Check whether it's valid:
        if form.is_valid():
            # Get the user info from the form data and login the user
            user = form.get_user()
            login(request, user)
            # Redirect the user to index page
            if request.user.is_superuser:
                return redirect('index')
            return redirect('profile')
    else:
        # Create an empty instance of Django's AuthenticationForm to generate the necessary html on the template.
        form = AuthenticationForm()
    return render(request, 'tutor/index.html', {'form': form})





"""Controller for Tutor registration page"""
def register_view(request):
    # This function renders the registration form page and create a new user based on the form data
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        # Check whether it's valid: for example it verifies that password1 and password2 match
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


"""Controller for User Agreement page"""
def useragreement_view(request):
    # Display user agreement
    return render(request, 'tutor/useragreement.html')


"""Controller for Tutor Activation landing page"""
def activate(request, uidb64, token):
    # Activate tutor account via link from their email
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


"""Controller for Tutor password reset request page"""
def password_reset_request(request):
    # Display form for password reset and send email with link to reset password
	if request.method == "POST":
        # Using Django's default password reset form
		password_reset_form = PasswordResetForm(request.POST)
        # Send email
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
						send_mail(subject, email, 'no.reply.accelerated.learning@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ('password_reset_done')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="tutor/password/password_reset.html", context={"password_reset_form":password_reset_form})


"""Controller for Tutor profile view page"""
@login_required(login_url='login')
def profile_view(request):
    # Tutor profile page
    user = User.objects.get(email=request.user.email)
    tutor = Tutor.objects.filter(email=user)
    return render(request, 'tutor/profile.html', {'authenticated': True, "Tutor": tutor, "User": user})


"""Controller for deleting 'personal' tutor account"""
@login_required(login_url='login')
def del_account(request):
    # Delete account and redirect to login page
    current =User.objects.get(id=request.user.id)
    current.tutor.resume.delete()
    current.tutor.image.delete()
    current.delete()
    return redirect('login')

"""Controller for Tutor logout"""
def logout_view(request):
    # Log out tutor
    logout(request)
    return redirect('login')




"""The following are Controllers for the edit pages"""
# These Views are very similar and could be refactored into one view with if/elif statements



"""Edit Personal Page"""
@login_required(login_url='login')
def edit_personal_view(request):
    # Edit personal information
    profiles = Tutor.objects.get(email_id=request.user.id)
    form = tutorPersonalform(request.POST or None, instance=profiles)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'tutor/personal.html', {'authenticated': True, 'form': form})


"""Edit Education Page"""
@login_required(login_url='login')    
def edit_edu_view(request):
    # Edit education section
    profiles = Tutor.objects.get(email_id=request.user.id)
    form = tutorEduform(request.POST or None, instance=profiles)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'tutor/edu.html', {'authenticated': True, 'form': form})


"""Edit Work Experience Page"""
@login_required(login_url='login')
def edit_work_view(request):
    # Edit work information
    profiles = Tutor.objects.get(email_id=request.user.id)
    form = tutorWorkform(request.POST or None, instance=profiles)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'tutor/work.html', {'authenticated': True, 'form': form})


"""Edit QA Page"""
@login_required(login_url='login')
def edit_qa_view(request):
    # Edit questionnaire section
    profiles = Tutor.objects.get(email_id=request.user.id)
    form = tutorQAform(request.POST or None, instance=profiles)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'tutor/qa.html', {'authenticated': True, 'form': form})


"""Edit File Upload Page"""
@login_required(login_url='login')
def imgUpload_view(request):
    # Upload documents
    profiles = Tutor.objects.get(email_id=request.user.id)
    form = imageUpload(request.POST or None, request.FILES or None, instance=profiles)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'tutor/imgUpload.html', {'authenticated': True, 'form': form})
