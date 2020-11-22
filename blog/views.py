from django.shortcuts import render
from .models import News

# news = [
#     {'title': 'Наша первая запись',
#      'text': 'Просто большой текст для 1 записи',
#      'date': '1 января 2019',
#      'author': 'Георгий'
#      },
#
#     {'title': 'Наша вторая запись',
#      'text': 'Просто большой текст для 2 записи',
#      'date': '10 января 2019'
#      },
# ]


def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Главная страница блога'
    }
    return render(request, 'blog/home.html', data)


def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'Страница про нас'})
