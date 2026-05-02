from django.db import models


class poem(models.Model):
    STANZA = models.TextField()
    pub_date = models.DateTimeField("date published")
    likes = models.IntegerField(default=0)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

