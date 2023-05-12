from django.shortcuts import render
import datetime


def render_indexpage(request):
    date = datetime.datetime.now()
    return render(request, 'page/index.html', {
        'date':date,
        })