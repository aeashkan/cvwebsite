from django.shortcuts import render, redirect
from django.http import HttpResponse
from website.forms import ContactForm
from django.contrib import messages


# Create your views here.


def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):

    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() and messages.success(request, 'پیام شما ارسال شد')
        else:
            return redirect('/contact')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})
