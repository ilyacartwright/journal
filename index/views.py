from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime

from school.models import Employees, Items
from users.forms import AuthForm


@login_required(login_url="index:login")
def render_indexpage(request):
    employees = Employees.objects.get(user=request.user)
    classes = Items.objects.filter(teacher=employees)

    def filters(self):
        for item in classes.filter():
            return item.classes

    return render(
        request,
        "page/auth/index.html",
        {"employees": employees, "classes": filters(request)},
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
