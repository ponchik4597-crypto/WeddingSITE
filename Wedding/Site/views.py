from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Guest
from .forms import GuestForm


def main(request):
    return render(request, "site/main.html")


def location(request):
    return render(request, "site/location.html")


def dress_code(request):
    return render(request, "site/dress_code.html")


def presence(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'site/thanks.html')  # после успешной отправки
    else:
        form = GuestForm()
    return render(request, 'site/presence.html', {'form': form})


def thank_you(request):
    return render(request, 'site/thanks.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена<h1>")
