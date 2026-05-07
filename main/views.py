import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.db.models import F,Q
from pytz import timezone
from .models import poem
import random


def index(request):
    action = request.GET.get('action')
    print(action)
    if action is None:
        pass
    elif 'like+'in action:
        stanza_id = action.split('+')[1]
        update = poem.objects.filter(id=stanza_id).update(likes=F('likes') + 1)
    
    elif action == 'skip':
        pass
    elif 'delete_poem' in action:
        stanza_id = action.split('+')[1]
        poem.objects.filter(id=stanza_id).delete()

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
    if request.user.is_authenticated:
        poems = poem.objects.filter(author=request.user)
        context = {"poems": poems}
    else:
        context = {"poems": []}
    return render(request, "profile.html", context)


def login(request):
    return render(request, "LOGIN.html")

def poem_detail(request, poem_id):
    poem_instance = poem.objects.get(id=poem_id)
    context = {"poem": poem_instance}
    return render(request, "poem_detail.html", context)

def submit_poem(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title")
        content = data.get("content")

        if title and content:
            poem.objects.create(title=title, STANZA=content, author=request.user.username)
            return JsonResponse({"status": "success", "redirect": "/profile"})
        else:
            return JsonResponse({"status": "error", "message": "Title and content are required."})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."})

def search_results(request):
    query = request.GET.get('q', '')
    search_type = request.GET.get('type', 'general')
    print(f"Search query: {query}, Search type: {search_type}")
    if search_type.lower() == 'author':
        poems = poem.objects.filter(author__icontains=query)
    elif search_type.lower() == 'title':
        poems = poem.objects.filter(title__icontains=query)
    else:
        poems = poem.objects.filter(Q(title__icontains=query) | Q(STANZA__icontains=query) | Q(author__icontains=query))
    context = {"poems": poems, "query": query, "search_type": search_type}
    return render(request, "search_results.html", context)