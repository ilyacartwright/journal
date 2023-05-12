from django.urls import path
from .views import render_indexpage

app_name = 'index'


urlpatterns = [
    path('', render_indexpage, name="home"),

]
