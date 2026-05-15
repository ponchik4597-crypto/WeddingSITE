from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import GuestForm


def main(request):
    return render(request, "site/main.html")


def details(request):
    return render(request, "site/details.html")


def presence(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            guest_presence = form.cleaned_data.get('presence')
            if guest_presence == 'no':
                return redirect('not_coming')
            return redirect('thank_you')
    else:
        form = GuestForm()
    return render(request, 'site/presence.html', {'form': form})


def thank_you(request):
    return render(request, 'site/thanks.html')


def not_coming(request):
    return render(request, 'site/not_coming.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена<h1>")
