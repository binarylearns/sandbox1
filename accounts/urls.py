from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(
        template_name="accounts/login.html"
    ), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),
    path("classes/", views.classes, name="classes"),
    path("lab-practical/", views.lp, name="lab_practical"),
    path("1st/", views.f1st, name="1stst"),

    path("english_typing/", views.english_typing, name="english_typing"),



]