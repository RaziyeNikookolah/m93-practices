from django.urls import path
from . import views

urlpatterns = [
    path('all_posts/', views.all_posts,name='all_posts'),
    path('post_details/<int:post_id>/', views.post_details, name='post_details'),
]
