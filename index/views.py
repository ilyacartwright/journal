from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime

from school.models import Employees
from users.forms import AuthForm


@login_required(login_url="index:login")
def render_indexpage(request):
    employees = Employees.objects.filter(user=request.user)
    date = datetime.datetime.now()

    return render(
        request,
        "page/auth/index.html",{
        'date': date,
        'employees': employees,
        },
    )


class LoginUser(LoginView):
    form_class = AuthForm
    template_name = "page/index.html"

    def get_success_url(self):
        return reverse_lazy("index:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date"] = datetime.datetime.now()
        return context


def logout_view(request):
    logout(request)
    return redirect("index:login")
