from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat_view, name="satgpt"),
    path("get-response/", views.get_response, name="satgpt_response"),
]
