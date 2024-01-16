from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from mysite.models import Contact
from mysite.forms import ContactFrom, SubscibeForm
from django.contrib import messages

def index(request):
    return render(request, 'mysite/index.html')

def contact(request):
    form = ContactFrom()
    if request.method == "POST":
        form = ContactFrom(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your ticket has been issued.")

            return HttpResponseRedirect(reverse('mysite:index'))
        else:
            messages.add_message(request, messages.ERROR, 'Your ticket was not issued.')


    return render(request, 'mysite/page-contact.html', {'form': form})

def subscibe(request):
    if request.method == "POST":
        form = SubscibeForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "You Subscribed Successfully.")
        else:
            messages.add_message(request, messages.WARNING, "Enter your email correctly.")
    return HttpResponseRedirect(reverse('mysite:index'))

def about(request):
    return render(request, 'mysite/about.html')

def sitemap(request):
    return render(request, 'mysite/page-sitemap.html')


def test2(request):
    form = ContactFrom()

    if request.method == "POST":
        form = ContactFrom(data=request.data)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            Contact.objects.create(name=name, email=email, phone_number=phone_number,
                                    subject=subject, message=message)
            return HttpResponseRedirect(reverse('mysite:index'))
    
    return render(request, 'test2.html', {'form':form})