from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect 
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Work, Comment, Exhibit, Gallery

# Create your views here.

def IndexView(request):
    context = {}
    try:
        galleries = Gallery.objects.filter(curator=request.user)
        context['gallery_list'] = galleries
    except:
        pass
    try:
        works = Work.objects.filter(collected_by=request.user)
        context['work_list'] = works
    except:
        pass
    context = {'work_list':works, 'gallery_list':galleries}
    return render(request, template_name='collector/index.html', context=context)

class WorkCreateView(LoginRequiredMixin, CreateView):
    model = Work
    fields = ['figure', 'title', 'description', 'subject_matter']
    template_name = 'collector/create.html'
    success_url = '/collector/'

    def form_valid(self, form):
        form.instance.collected_by = self.request.user
        return super().form_valid(form)

class WorkUpdateView(LoginRequiredMixin, UpdateView):
    model = Work 
    fields = ['artist', 'figure', 'title', 'description', 'subject_matter']
    template_name = 'collector/create.html'

class WorkDeleteView(LoginRequiredMixin, DeleteView):
    model = Work 
    success_url = reverse_lazy('collector:work-list')

class WorkListView(LoginRequiredMixin, ListView):
    context_object_name = 'work_list'

    def get_queryset(self):
        return Work.objects.filter(collected_by=self.request.user)

class WorkDetailView(LoginRequiredMixin, DetailView):
    model = Work
    template_name = 'collector/work_detail.html'

class GalleryCreateView(LoginRequiredMixin, CreateView):
    model = Gallery
    fields = ['title', 'curatorial_statement']
    template_name = 'collector/create.html'

    def form_valid(self, form):
        form.instance.curator = self.request.user
        return super().form_valid(form)

class GalleryUpdateView(LoginRequiredMixin, UpdateView):
    model = Gallery 
    fields = ['title', 'curator']

class GalleryDeleteView(LoginRequiredMixin, DeleteView):
    model = Gallery 
    success_url = reverse_lazy('collector:gallery-list')

class GalleryDetailView(LoginRequiredMixin, DetailView):
    model = Gallery
    template_name = 'collector/gallery_detail.html'

class ExhibitCreateView(LoginRequiredMixin, CreateView):
    model = Exhibit
    fields = ['title', 'curatorial_statement']
    template_name = 'collector/create.html'

    def form_valid(self, form):
        form.instance.curator = self.request.user
        form.instance.gallery_id = self.kwargs['pk']
        return super().form_valid(form)

class ExhibitUpdateView(LoginRequiredMixin, UpdateView):
    model = Exhibit 
    fields = ['title', 'curatorial_statement']
    template_name = 'collector/create.html'

class ExhibitDeleteView(LoginRequiredMixin, DeleteView):
    model = Exhibit 
    success_url = reverse_lazy('collector:exhibit-list')

class ExhibitDetailView(LoginRequiredMixin, DetailView):
    model = Exhibit
    template_name = 'collector/exhibit_detail.html'

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['comment_text']
    template_name = 'collector/create.html'
    work_id = ''

    def form_valid(self, form):
        form.instance.commentor = self.request.user
        form.instance.work_id = self.kwargs['work_id']
        return super().form_valid(form)