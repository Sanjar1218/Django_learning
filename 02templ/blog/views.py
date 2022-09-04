from django.shortcuts import render

lst = [
    {
        'name': 'Blog post 1',
        'author': 'CorayMS',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'name': 'Blog post 2',
        'author': 'Jane Doe',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
    
]
# Create your views here.
def home(request):
    context = {
        'posts': lst
    }
    return render(request, 'pages/home.html', context=context)

def about(request):
    return render(request, 'pages/about.html')