# This is the url path for the Tutor app, 
# All the the urls specified in this file will be accessible to the users/tutors 
from . import views
from django.urls import path
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView


urlpatterns = [
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('register/', views.register_view, name='register'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='tutor/password/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="tutor/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='tutor/password/password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('edit/personal', views.edit_personal_view, name='personal'),
    path('edit/edu', views.edit_edu_view, name='edu'),
    path('edit/work', views.edit_work_view, name='work'),
    path('edit/qa/', views.edit_qa_view, name='qa'),
    path('profile/', views.profile_view, name='profile'),
    path('delete/', views.del_account, name='delete'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/imgUpload/', views.imgUpload_view, name='imgUpload'),
    path('useragreement/', views.useragreement_view, name='useragreement'),
]
