from django.urls import path

from .views import read_message, write_message

urlpatterns = [
    path("write/<device>/<message>/", write_message, name="write_message"),
    path("read/", read_message, name="read_message"),
]
