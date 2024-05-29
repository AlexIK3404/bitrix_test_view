from django.urls import path
from . import views

urlpatterns = [
    path("generate_video/<str:text>", views.generate_running_line),
]
