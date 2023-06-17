from django.shortcuts import render
from .forms import PostCreateForm
from django.http import HttpResponse


# Create your views here.
def create(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        form = PostCreateForm()
        return render(request, 'home/create.html', {'form': form})


def index(request):
    return  HttpResponse("<h3>heloooo</h3>")
