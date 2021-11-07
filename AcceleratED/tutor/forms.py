from django import forms
####USER PAGE VVVVV
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from tutor.models import Tutor



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']


class tutorIntakeform(forms.ModelForm):
    class Meta:
        model =Tutor
        fields = ('firstname', 'lastname', 'phonenumber', 'birthday', 'gender',
                'introduction', 'languages','education', 'major',
                'minor', 'experience', 'statecert', 'phonicsex', 'employment',
                'curremployment', 'employer', 'employeraddress', 'currreference',
                'teachercharacteristics', 'abilitiesquestion', 'availability'
                )
        
        