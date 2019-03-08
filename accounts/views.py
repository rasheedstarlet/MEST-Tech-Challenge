from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.forms import UserCreationForm
# Create your views here.

from . forms import LoginForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home:home")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {'form':form})


def user_login(request):
    if request.method == "POST":
        user_form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'],
                                password = cd['password'])
            if user is None:
                if user.is_active():
                    login(request, user)
                else:
                    HttpResponse("Disabled Account")
            else:
                HttpResponse("Invalid Login")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html', {})
