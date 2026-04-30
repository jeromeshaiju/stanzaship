from django.urls import path

from . import views


# this is to register in the namebase of the app so that we can use it in the templates
app_name = 'main'

urlpatterns = [
    path("", views.index, name="index"),
    path("write", views.write, name="write"),
    path("profile", views.profile, name="profile"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
]