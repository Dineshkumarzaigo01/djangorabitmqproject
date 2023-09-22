from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .forms import SendEmailForm
from .tasks import send_email_task, webhook_info # we will define this function later

from anyjson import serialize
import requests
import json


def index(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        if form.is_valid():      
            email = form.cleaned_data['email']
            send_email_task.delay(email)
            return render(request, 'index.html', {'form': form})
            

    form = SendEmailForm()
    return render(request, 'index.html', {'form': form})


def webhook_send_info(request):
    webhook_url = 'https://webhook.site/67a0d69d-e48c-43f9-86dd-ca2aba286ba6'
    webhook_info.delay(webhook_url)
    return HttpResponse("success")
    
    




def multiply(request):
    x = int(request.GET['x'])
    y = int(request.GET['y'])
    result = x * y
    response = {'status': 'success', 'retval': result}
    return HttpResponse(serialize(response), mimetype='application/json')



