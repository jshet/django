from django.db import models

# Create your models here.

class Artifact(models.Model):
    artifact_name = models.CharField(max_length=200)
    collected_date = models.DateTimeField('date collected')

    def __str__(self):
        return self.artifact_name

class Comment(models.Model):
    artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500)
    reactions = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text


