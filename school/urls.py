from django.urls import path
from .views import SchoolView


app_name = "school"

urlpatterns = [
    path("<int:pk>", SchoolView.as_view(), name="school"),
]
