from django.contrib.auth import get_user_model, logout
from django.shortcuts import redirect, render

from tutor.models import Tutor




# Create your views here.


# def index_view_order(request):
#     if request.user.is_superuser:
#         User = get_user_model()
#         if request.method == "POST":
#             ordered = request.POST['order']
#             user = User.objects.order_by(ordered)
#         else:
#             user = User.objects.all()
#         return render(request, 'owner/index.html', { "User": user})
#     else: 
#         return redirect('login')

def index_view(request):
    if request.user.is_superuser:
        User = get_user_model()
        if request.method == "POST":  
            searched =request.POST['searched'] 
            by =request.POST['by']
            search_type = 'contains'
            filter = by + '__' + search_type
            ordered = request.POST['order']
            print("this is a line")
            print(request.POST.getlist('px'))
            px = request.POST.getlist('px')
            user = User.objects.filter(
                **{filter: searched}).order_by(ordered).filter(tutor__phonicsex__contains=', '.join(px))
            # user = User.objects.filter(tutor__phonicsex__contains= 'Lalilo')

        else:
            user = User.objects.all()
        return render(request, 'owner/index.html', { "User": user})
    else: 
        return redirect('login')


def del_account(request, id):
    User = get_user_model()
    current = User.objects.get(id=id)
    current.delete()
    return redirect('index')

def profile_view(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)
    return render(request, 'owner/profile.html', {'authenticated': True, "User": user})

def logout_view(request):
    logout(request)
    return redirect('login')
