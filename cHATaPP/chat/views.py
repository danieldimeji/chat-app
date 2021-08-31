from django.shortcuts import render


def home_view(request):
    print(request.user)
    context = {

    }
    return render(request, 'index.html', context)
