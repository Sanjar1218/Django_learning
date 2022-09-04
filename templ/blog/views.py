from django.shortcuts import render

lst = [
    {
        'name': 'Jane Doe',
        'age': 23,
        'job': 'devoloper',
        'text': 'asdfaefa dafef ad'
    },
    {
        'name': 'Sanjarbek Saidov',
        'age': 20,
        'job': 'backend',
        'text': 'a;slkfjaef iasd;fkljae;f iajd;flkaj ;elkfj ae'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts': lst
    }
    return render(request, 'pages/home.html', context=context)

def room(request):
    return render(request, 'pages/room.html')