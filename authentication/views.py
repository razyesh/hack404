from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'base.html')
            else:
                return render(request, 'login.html', {'message':'You are not active user'})
        else:
            return render(request, 'login.html', {'message':'Invalid Login Credentials'})

    return render(request, 'login.html') 


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login.html', context)


