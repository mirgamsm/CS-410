from django.contrib.auth import get_user_model, logout
from django.shortcuts import redirect, render

from tutor.models import Tutor

def index_view(request):
    if request.user.is_superuser:
        User = get_user_model()
        if request.method == "POST":  
            searched =request.POST['searched'] 
            by =request.POST['by']
            search_type = 'contains'
            filter = by + '__' + search_type
            ordered = request.POST['order']
            avail = request.POST.getlist('avail')
            cert = request.POST.getlist('cert')
            px = request.POST.getlist('px')
            edu = request.POST.getlist('edu')
            user = User.objects.filter(
                **{filter: searched}).order_by(ordered)
            for a in avail:
                user =user.filter(tutor__availability__contains=a)
            for c in cert:
                user =user.filter(tutor__experience__contains=c)
            for p in px:
                user =user.filter(tutor__phonicsex__contains=p)
            for e in edu:
                user =user.filter(tutor__education__contains=e)

        else:
            user = User.objects.all()
        return render(request, 'owner/index.html', { "User": user})
    else: 
        return redirect('login')


def del_account(request, id):
    User = get_user_model()
    current = User.objects.get(id=id)
    current.tutor.resume.delete()
    current.tutor.image.delete()
    current.delete()
    return redirect('index')

def profile_view(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)
    return render(request, 'owner/profile.html', {'authenticated': True, "User": user})

def logout_view(request):
    logout(request)
    return redirect('login')
