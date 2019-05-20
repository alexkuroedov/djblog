from django.shortcuts import render
from django.http import HttpResponse

news = [
    {'title': 'Our First News',
     'text': 'Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley',
     'date': '01 20 2019',
     'author': 'Alex'
     },

    {'title': 'Our Second News',
     'text': 'Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley',
     'date': '01 20 2019',
     },
]


# Create your views here.
def home(request):
    data = {
        'news': news,
        'title': 'Main Blog Page'
    }
    return render(request, 'blog/home.html', data)


def contacts(request):
    return render(request, 'blog/contacts.html', {'title':'About us page'})
    # return HttpResponse('Contacts Page')
