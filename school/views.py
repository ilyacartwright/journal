from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime


from settings.models import Schools
from .models import Employees
from school_menu.models import Sites, Partners


class SchoolView(LoginRequiredMixin, DetailView):
    login_url = "index:login"
    model = Schools
    template_name = "school/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # import ipdb; ipdb.set_trace()
        
        context["employees"] = Employees.objects.filter(user=self.request.user)
        context["menu_partners"] = Partners.objects.filter(school=self.object)
        context["menu_sites"] = Sites.objects.filter(school=self.object)
        context['date'] = datetime.datetime.now()
        return context
    
