from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.name


class poem(models.Model):
    STANZA = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    likes = models.IntegerField(default=0)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, blank=True)