# This is the url path for the Tutor app, 
# All the the urls specified in this file will be accessible to the users/tutors 
from . import views
from django.urls import path

urlpatterns = [

    path('register/', views.register_view, name='register'),
    path('edit/', views.register_view, name='register'),
    path('profile/', views.register_view, name='register'),
]
