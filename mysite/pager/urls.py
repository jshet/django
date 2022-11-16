from django.urls import path

from .views import IndexView, SourceListView, SourceDetailView

app_name = 'pager'
urlpatterns = [
    path('', IndexView, name='index'),
    path('sources', SourceListView.as_view(template_name='pager/source_list.html'), name='source-list'),
    path('source/<int:pk>/', SourceDetailView.as_view(template_name='pager/source_detail.html'), name='source-detail'),
]