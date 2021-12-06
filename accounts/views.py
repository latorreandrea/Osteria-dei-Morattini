from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from .forms import UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    else:
        if request.method == 'POST':
            user_form = UserLoginForm(request.POST)
            if user_form.is_valid():
                user = auth.authenticate(request.POST['username_or_email'],
                                         password=request.POST['password'])

                if user:
                    auth.login(request, user)
                    messages.success(
                        request, "You have successfully logged in")

                    if request.GET and request.GET['next'] != '':
                        next = request.GET['next']
                        return HttpResponseRedirect(next)
                    else:
                        return redirect(reverse('index'))
                else:
                    user_form.add_error(
                        None, "Your username or password are incorrect")
            else:
                user_form = UserLoginForm()
        else:
            user_form = UserLoginForm()

        args = {'user_form': user_form, 'next': request.GET.get('next', '')}
        return render(request, 'login.html', args)


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    logout(request)
    # messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))