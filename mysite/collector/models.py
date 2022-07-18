from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.

class Work(models.Model):
    artist = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200)
    subject_matter = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField('date added', auto_now_add=True)
    date_updated = models.DateTimeField('date updated', auto_now=True)
    collected_by = models.ForeignKey(User, on_delete=models.CASCADE)
    figure = models.ImageField(upload_to='images/', null=True, blank=True)
    variant_of = models.ForeignKey('self', related_name='variant_of_work', null=True, blank=True, on_delete=models.CASCADE)
    fragment_of = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    collected_from = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    comment_text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    reactions = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text

    def get_absolute_url(self):
        return reverse('collector:work-detail', args=[self.work_id])

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_opened = models.DateTimeField(default=datetime.now)
    date_closed = models.DateTimeField(default=datetime.now)
    curator = models.ForeignKey(User, on_delete=models.CASCADE)
    curatorial_statement = models.TextField()
    contributors = models.ManyToManyField(User, related_name='contributors')
    guest_list = models.ManyToManyField(User, related_name='guests')

    def __str__(self):
        return self.title

class Exhibit(models.Model):
    title = models.CharField(max_length=200)
    curator = models.ForeignKey(User, on_delete=models.CASCADE)
    curatorial_statement = models.TextField()
    works = models.ManyToManyField(Work)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        