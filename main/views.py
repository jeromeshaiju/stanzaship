from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.db.models import F,Q
from .models import poem
import random


def index(request):
    action = request.GET.get('action')
    # Handle button actions
    #nothing for now but should log into db later on
    print(action)

    if action is None:
        pass
    elif 'like+'in action:
        stanza_id = action.split('+')[1]
        update = poem.objects.filter(id=stanza_id).update(likes=F('likes') + 1)
    
    elif action == 'skip':
        pass

    count = poem.objects.count()
    if count == 0:
        random_stanza = None
    else:
        random_id = random.randint(1, count)
        random_stanza = poem.objects.filter(pk__gte=random_id).first()
    context = {"stanza": random_stanza}
    return render(request, "stanzareels.html", context)



# HAVE USED QUILL FOR THE TEXT EDDITOR IN THE PAST, CAN USE IT AGAIN
def write(request):
    return render(request, "write.html")

def profile(request):
    return render(request, "profile.html")


def signup(request):
    return render(request, "SIGNUP.html")


def login(request):
    return render(request, "LOGIN.html")
