from django.http.response import HttpResponse
from django.shortcuts import render

from accounts.models import *
from accounts.forms import *


def home_view(request):
    
    context = {

    }
    return render(request, 'index.html', context)


def settings_view(request):

    user = request.user
    user_profile = Profile.objects.get(user=user)
    form = EditProfileForm(
        instance = user_profile,
        initial = {
            'first_name':user.first_name,
            'last_name':user.last_name,
        }
    )

    if request.method == 'POST':
        
        form = EditProfileForm(request.POST or None, instance = user_profile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user.first_name = first_name
            user.last_name = last_name
            user.save(update_fields=['first_name', 'last_name'])
            form.save()
        else:
            print(form.errors)
  
    context = {
        'profile':user_profile,
        'form':form
    }
    return render(request, 'settings.html', context)


def groups_view(request):

    context = {

    }
    return HttpResponse('View')


def status_view(request):

    context = {

    }
    return HttpResponse('View')


def calls_view(request):

    context = {

    }
    return HttpResponse('View')


def archived_view(request):

    context = {

    }
    return HttpResponse('View')
