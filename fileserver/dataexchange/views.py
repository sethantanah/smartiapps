# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings
from django.core.mail import send_mail


@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        # Extract data from the request

        name = request.POST.get('name')
        email = request.POST.get('email')
        m_subject = request.POST.get('subject')
        message = request.POST.get('message')


        try:
            subject = f'{m_subject}:  {email}'
            message = f'You have received a new message from your website contact form.\n\n"."Here are the details:\n\nName: {name}\n\n\nEmail: {email}\n\nSubject: {m_subject}\n\nMessage: {message}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['smarticonsul@gmail.com']
            

            # Send the email
            response = send_mail( subject, message, email_from, recipient_list )
            # print(response.status_code)
            # print(response.body)
            # print(response.headers)
            return JsonResponse({'message': 'Email sent successfully'})
        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=500)

    return JsonResponse({'message': 'Invalid request method'}, status=400)
