from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect 
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from .models import Work, Comment

# Create your views here.

class WorkCreateView(LoginRequiredMixin, CreateView):
    model = Work
    fields = ['title']

    def form_valid(self, form):
        form.instance.collected_by = self.request.user
        return super().form_valid(form)

class WorkUpdateView(UpdateView):
    model = Work 
    fields = ['title']

class WorkDeleteView(DeleteView):
    model = Work 
    success_url = reverse_lazy('work-list')

class IndexView(ListView):
    template_name = 'collector/index.html'
    context_object_name = 'work_list'

    def get_queryset(self):
        return Work.objects.order_by('-collected_date')[:20]

class DetailView(DetailView):
    model = Work
    template_name = 'collector/detail.html'

class CommentFormView(CreateView):
    model = Comment
    fields = ['comment_text']
    template_name = 'collector/add_comment.html'

    def form_valid(self, form):
        work = get_object_or_404(Work, pk=self.kwargs['work_id'])
        work.comment_set.create(comment_text=form['comment_text'].as_text)

        return HttpResponseRedirect(reverse('collector:index'))

def vote(request, work_id):
    work = get_object_or_404(Work, work_id)
    work.votes += 1
    work.save()

    return HttpResponseRedirect(reverse('collector:detail', args=(work.id)))

def add_comment(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    form_comment_text = request.POST.get('comment_text')
    work.comment_set.create(comment_text=form_comment_text)
    return render(request, 'collector/detail.html', {'work':work})