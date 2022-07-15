from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class Work(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField('date added', auto_now_add=True)
    collected_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('work-detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    reactions = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text


