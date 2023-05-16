from django.urls import path
from .views import LoginUser, render_indexpage

app_name = 'index'


urlpatterns = [
    path('', render_indexpage, name="home"),
    path('index/', LoginUser.as_view(), name="login"),


]
