from django.http import HttpResponse

from .models import Message


# Create your views here.
def write_message(request, device, message):
    pass


def read_message(request):
    message = Message.objects.all().last()
    data = f"{message.message} | {message.device} | {message.created_at}"
    return HttpResponse(data)
