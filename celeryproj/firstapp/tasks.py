#tasks.py

from __future__ import absolute_import, unicode_literals


# from celery import shared_task

# @shared_task
# def add(x, y):
    # return x + y

import time
from celery import shared_task

from django.core.mail import send_mail
import requests
import json

# ...

@shared_task
def send_email_task(email):
    "background task to send an email asynchronously"
    subject = 'Helo from Celery'
    message = 'This is a test email sent asynchronously with Celery.'
    
    time.sleep(5)
    return send_mail(
        subject,
        message,
        'dineshkumar.m@zaigoinfotech.com',
        [email],
        fail_silently=False
    )

@shared_task
def webhook_info(url):
    webhook_url = url
    data = { 'name': 'webhook test', 
         'Channel URL': 'https://www.youtube.com/channel/UC4Snw5yrSDMXys31I18U3gg' }
    r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    