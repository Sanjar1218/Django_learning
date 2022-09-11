from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # print(context['posts'][0].author.profile)
    return render(request, 'pages/home.html', context=context)

def about(request):
    return render(request, 'pages/about.html')