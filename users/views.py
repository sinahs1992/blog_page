from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import messages
from django.shortcuts import render, redirect
from users.forms import CustomUserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been successfully logged out. Goodbye!")

        # Call the parent class's dispatch method to perform the logout
        response = super().dispatch(request, *args, **kwargs)

        # Return the response
        return response
    
class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "You have been successfully logged in!")
        return response

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserCreationForm(data=request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "You signed up successfully.")
                return HttpResponseRedirect(reverse("users:login"))
            else:
                messages.add_message(request,messages.ERROR, "Incorrect information entered")
                redirect("/")
    else:
        redirect("/")

    form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context)