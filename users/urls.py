from django.urls import path
from django.contrib.auth import views as auth_views
from core import settings
from users.views import CustomLogoutView, CustomLoginView
from users.views import signup_view

app_name = "users"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name="logout"),
    path("signup/", signup_view, name="signup")

]
