from django import forms
####USER PAGE VVVVV
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.db.models import fields

from tutor.models import Tutor



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']


class DateInput(forms.DateInput):
    input_type = 'date'

# class tutorIntakeform(forms.ModelForm):
#     class Meta:
#         model =Tutor
#         fields = ('firstname', 'lastname', 'birthday', 'phonenumber', 'gender',
#                 'introduction', 'languages','education', 'major',
#                 'minor', 'experience', 'statecert', 'phonicsex', 'employment',
#                 'curremployment', 'employer',
#                 'employeraddress', 'employercity', 'employerstate', 'employerzip',
#                 'currreference',
#                 'teachercharacteristics', 'abilitiesquestion', 'availability'
#                 )
#         widgets = { 'birthday' : DateInput()}
        

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
                'minor', 'experience', 'statecert', 'phonicsex', )


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
            'image',
        )