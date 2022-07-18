from django.urls import path

from .views import WorkCreateView, WorkUpdateView, WorkDeleteView, IndexView, DetailView, CommentCreateView, vote

app_name = 'collector'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('work/add/', WorkCreateView.as_view(), name='work-add'),
    path('work/<int:pk>/edit/', WorkUpdateView.as_view(), name='work-update'),
    path('work/<int:pk>/delete/', WorkDeleteView.as_view(), name='work-delete'),
    path('<int:pk>/', DetailView.as_view(), name='work-detail'),
    path('<int:work_id>/add_comment/', CommentCreateView.as_view(work_id='work_id'), name='comment-add'),
    path('<int:work_id>/vote/', vote, name='vote')
]