from django.urls import path

from .views import IndexView
from .views import WorkCreateView, WorkUpdateView, WorkDeleteView, WorkListView, WorkDetailView, CommentCreateView 
from .views import GalleryListView, GalleryCreateView, GalleryDeleteView, GalleryUpdateView, GalleryDetailView
from .views import ExhibitListView, ExhibitCreateView, ExhibitDeleteView, ExhibitUpdateView, ExhibitDetailView

app_name = 'collector'
urlpatterns = [
    path('', IndexView, name='index'),
    path('work/', WorkListView.as_view(), name='work-list'),
    path('work/<int:pk>/', WorkDetailView.as_view(), name='work-detail'),
    path('work/add/', WorkCreateView.as_view(), name='work-add'),
    path('work/<int:pk>/edit/', WorkUpdateView.as_view(), name='work-update'),
    path('work/<int:pk>/delete/', WorkDeleteView.as_view(), name='work-delete'),
    path('<int:work_id>/add_comment/', CommentCreateView.as_view(work_id='work_id'), name='comment-add'),
    path('gallery/', GalleryListView.as_view(), name='gallery-list'),
    path('gallery/add/', GalleryCreateView.as_view(), name='gallery-add'),
    path('gallery/<int:pk>/', GalleryDetailView.as_view(), name='gallery-detail'),
    path('gallery/<int:pk>/edit/', GalleryUpdateView.as_view(), name='gallery-update'),
    path('gallery/<int:pk>/delete/', GalleryDeleteView.as_view(), name='gallery-delete'),
    path('gallery/<int:pk>/exhibit/add/', ExhibitCreateView.as_view(), name='exhibit-add'),
    path('gallery/exhibit/', ExhibitListView.as_view(), name='exhibit-list'),
    path('gallery/exhibit/<int:pk>/', ExhibitDetailView.as_view(), name='exhibit-detail'),
    path('gallery/exhibit/<int:pk>/edit/', ExhibitUpdateView.as_view(), name='exhibit-update'),
    path('gallery/exhibit/<int:pk>/delete/', ExhibitDeleteView.as_view(), name='exhibit-delete'),
]