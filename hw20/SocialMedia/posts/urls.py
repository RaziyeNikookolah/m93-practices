from django.urls import path
from . import views

urlpatterns = [
    path('all_posts/', views.all_posts, name='all_posts'),
    path('post_details/<int:post_id>/', views.post_details, name='post_details'),
    path('user_posts/<int:user_id>/', views.user_posts, name='user_posts'),
    path('add_post/<int:user_id>',views.add_post,name='add_post')
]
