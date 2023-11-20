# urls.py
from django.urls import path
from .views import send_email, email_list

urlpatterns = [
    path('send-email/', send_email, name='send_email'),
    path('email-list/',  email_list, name='email_list')
]
