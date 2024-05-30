from django.urls import path
from . import views

urlpatterns = [
    path("<str:text>", views.generate_running_line),
]
