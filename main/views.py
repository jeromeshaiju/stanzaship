from django.http import HttpResponse
from django.shortcuts import render
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
    return render(request, "index.html", context)