from django.urls import path

from django.conf import settings
from django.conf.urls.static import static 

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('flower/<slug:slug>/', views.detail_page, name='detail-page'),
    path('tags/<slug:slug>/',views.tags, name='tags'),
    path('flower-create/',views.create_page, name='create'),
    path('flower/<int:pk>/edit', views.edit_page, name='edit'),    
    path('flower/<int:pk>/delete/', views.delete_flower, name='delete'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)