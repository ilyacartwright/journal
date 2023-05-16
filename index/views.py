from django.shortcuts import render
import datetime
from django.contrib.auth.forms import AuthenticationForm
from users.forms import AuthForm


def render_indexpage(request):
    if request.user.is_authenticated:
        return render(request, 'page/auth/index.html', {})
    else:
        date = datetime.datetime.now()
        form = AuthForm()
        return render(request, 'page/index.html', {
            'date':date,
            'form': form,
            })