from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


# Create your models here.

class Source(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200)
    topic = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField('date added', auto_now_add=True)
    date_updated = models.DateTimeField('date updated', auto_now=True)
    collected_by = models.ForeignKey(User, on_delete=models.CASCADE)
    figure = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pager:source-detail', args=[self.id])