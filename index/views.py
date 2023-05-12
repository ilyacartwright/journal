from django.shortcuts import render


def render_indexpage(request):

    return render(request, 'page/index.html', {})