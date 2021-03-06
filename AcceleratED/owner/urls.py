# This is the url path for the Owner app,
# All the the urls specified in this file will be accessible to the Admin
from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:id>', views.profile_view, name='file'),
    path('delete/<int:id>', views.del_account, name='delete'),
]
