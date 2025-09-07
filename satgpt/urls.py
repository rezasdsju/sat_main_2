from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat_view, name="satgpt"),
    path("get-response/", views.get_response, name="satgpt_response"),
    path("clear-chat/", views.clear_chat_history, name="clear_chat_history"),
]