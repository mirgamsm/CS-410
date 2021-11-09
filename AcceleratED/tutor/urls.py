# This is the url path for the Tutor app, 
# All the the urls specified in this file will be accessible to the users/tutors 
from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('edit/', views.edit_view, name='edit'),
    path('profile/', views.profile_view, name='profile'),
    path('delete/', views.del_account, name='delete'),
    path('logout/', views.logout_view, name='logout')
]
