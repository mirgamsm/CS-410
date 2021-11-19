from django.contrib.auth import get_user_model, logout
from django.shortcuts import redirect, render

from tutor.models import Tutor

# Create your views here.



def index_view(request):
    if request.user.is_superuser:         
        User = get_user_model()
        user = User.objects.all()
        tutor = Tutor.objects.filter(email=user)
        return render(request, 'owner/index.html', {"Tutor": tutor, "User": user})
    else: 
        return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('login')
