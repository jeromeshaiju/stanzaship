from django.http import HttpResponse
from django.shortcuts import render
from .models import poem



def index(request):
    latest_stanza_list = poem.objects.order_by("-pub_date")[:5]
    context = {"latest_stanza_list": latest_stanza_list}
    return render(request, "index.html", context)