from django.shortcuts import render
import datetime
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from users.forms import AuthForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='index:login')
def render_indexpage(request):
        return render(request, 'page/auth/index.html', {})

    
class LoginUser(LoginView):
    form_class = AuthForm
    template_name = 'page/index.html'


    def get_success_url(self):
        return reverse_lazy('index:home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date"] = datetime.datetime.now()
        return context
    