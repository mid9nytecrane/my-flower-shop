from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('flower/<slug:slug>/', views.detail_page, name='detail-page'),
    path('tags/<slug:slug>/',views.tags, name='tags'),
    path('flower-create/',views.create_page, name='create'),
    path('flower/<int:pk>/edit', views.edit_page, name='edit'),    
    path('flower/<int:pk>/delete/', views.delete_flower, name='delete'),
]