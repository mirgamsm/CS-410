# This is the url path for the Tutor app, 
# All the the urls specified in this file will be accessible to the users/tutors 
from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('edit/', views.edit_view, name='edit'),
    path('edit/personal', views.edit_personal_view, name='personal'),
    path('edit/edu', views.edit_edu_view, name='edu'),
    path('edit/work', views.edit_work_view, name='work'),
    path('edit/qa/', views.edit_qa_view, name='qa'),
    path('profile/', views.profile_view, name='profile'),
    path('delete/', views.del_account, name='delete'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/imgUpload/', views.imgUpload_view, name='imgUpload'),
]
