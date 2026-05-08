from django.contrib import admin
from .models import poem, Tag

admin.site.register(poem)
admin.site.register(Tag)