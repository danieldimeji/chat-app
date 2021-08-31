from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .forms import *



def sign_up_view(request):

    if request.method == 'POST':

        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors, 'Not saved')

    context = {
        'form':SignUpForm
    }
    return render(request, 'sign-up.html', context)


def sign_in_view(request):

    if request.method == 'POST':

        form = SignInForm(request.POST or None)
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                return redirect('home')
            else:
                print(form.errors)
        else:
            print(form.errors)

    context = {
        'form':SignInForm
    }
    return render(request, 'sign-in.html', context)