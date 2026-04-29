from django.urls import path

from . import views


# this is to register in the namebase of the app so that we can use it in the templates
app_name = 'main'

urlpatterns = [
    path("", views.index, name="index"),
]