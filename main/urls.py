from django.urls import path

from . import views


# this is to register in the namebase of the app so that we can use it in the templates
app_name = 'main'

urlpatterns = [
    path("", views.index, name="index"),
    path("write", views.write, name="write"),
    path("profile", views.profile, name="profile"),
    path("login", views.login, name="login"),
    path("poem_detail/<int:poem_id>/", views.poem_detail, name="poem_detail"),
    path("submit_poem/", views.submit_poem, name="submit_poem"),
    path("search_results/", views.search_results, name="search_results"),
]