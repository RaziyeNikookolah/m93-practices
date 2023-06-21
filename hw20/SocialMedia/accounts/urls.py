from django.urls import path
from . import views

urlpatterns = [
    path('all_users/', views.all_users,name='all_users'),
    path('user_details/<int:user_id>/', views.user_details, name='user_details'),

]