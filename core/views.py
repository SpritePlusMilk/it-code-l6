from django.shortcuts import render
import datetime
import requests
from .models import Worker


def index(request):
    context = {'date': datetime.date.today(),
               'paragraph1': requests.get('https://baconipsum.com/api/?type=all-meat&sentences=5&start-with-lorem=1&format=text').content,
               'paragraph2': requests.get('https://baconipsum.com/api/?type=all-meat&sentences=7&format=text').content}
    return render(request, 'core/index.html', context)


def employees(request):
    return render(request, 'core/employees-list.html')
