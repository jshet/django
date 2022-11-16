from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Source

# Create your views here.

def IndexView(request):
    context = {}
    return render(request, template_name='pager/index.html', context=context)


class SourceListView(LoginRequiredMixin, ListView):
    context_object_name = 'source_list'

    def get_queryset(self):
        return Source.objects.filter(collected_by=self.request.user)

class SourceDetailView(LoginRequiredMixin, DetailView):
    model = Source