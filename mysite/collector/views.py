from django.shortcuts import render

from .models import Artifact, Comment

# Create your views here.

def index(request):
    artifact_list = Artifact.objects.order_by('-collected_date')
    context = {'artifact_list': artifact_list}
    return render(request, 'collector/index.html', context)