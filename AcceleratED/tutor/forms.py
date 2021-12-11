from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.db.models import fields
from django.contrib.auth.forms import PasswordResetForm
from django.core.validators import validate_integer
from tutor.models import Tutor

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']


class DateInput(forms.DateInput):
    input_type = 'date'       

class tutorPersonalform(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ('firstname', 'lastname', 'birthday', 'phonenumber', 'gender',
                  'introduction', 'languages'
                  )
        widgets = {'birthday': DateInput()}

class tutorEduform(forms.ModelForm):
    class Meta:
        model =Tutor
        fields = ('education', 'major',
                'minor', 'experience', 'statecert', 'phonicsex', 'otherphonics'
                )

class tutorWorkform(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ('employment',
                  'curremployment', 'employer',
                  'employeraddress', 'employercity', 'employerstate', 'employerzip',
                  'currreference',
                  )
class tutorQAform(forms.ModelForm):
    class Meta:
        model =Tutor
        fields = (
                'teachercharacteristics', 'abilitiesquestion', 'availability'
                )
class imageUpload(forms.ModelForm):
    class Meta: 
        model= Tutor 
        fields =(
            'image','resume'
        )