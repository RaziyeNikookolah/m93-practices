from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Address


# Create your views here.
def all_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        return render(request, 'accounts/all_users.html', {'users': users})


def user_details(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(id=user_id)
        addresses = Address.objects.filter(user=user)
        return render(request, 'accounts/user_details.html', {'user': user, 'addresses': addresses})
