from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError

# Create your views here.

def signup(request):
    if request.method == "GET":
        return render(request, "security/signup.html", {
            "form": UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)  # Log the user in after successful registration

                # **Consistent Redirection to Home with reverse_lazy:**
                return redirect(reverse_lazy('core:home'))  # Use reverse_lazy for maintainability
            except IntegrityError:
                return render(request, "security/signup.html", {
                    'form': UserCreationForm,
                    "error": 'Username already exists'
                })
        else:
            return render(request, "security/signup.html", {
                'form': UserCreationForm,
                "error": 'Password do not match'
            })

def signout(request):
    logout(request)
    # **Redirection to Home after Sign Out:**
    return redirect(reverse_lazy('core:home'))  # Use reverse_lazy for maintainability

def signin(request):  # Corrected typo in function name
    if request.method == 'GET':
        return render(request, "security/signin.html", {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'security/signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            # **Redirection to Home after Sign In:**
            return redirect(reverse_lazy('core:home'))  # Use reverse_lazy for maintainability