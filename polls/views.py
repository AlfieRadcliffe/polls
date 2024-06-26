from django.http import HttpResponse

# polls/views.py

from django.shortcuts import render, get_object_or_404
from .models import Client
from .utilities import send_sms

def index(request):
    # Your view logic here
    return render(request, 'polls/index.html')