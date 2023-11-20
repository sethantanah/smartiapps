# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os

# # views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from .form import EmailListForm

@csrf_exempt
def email_list(request):
    if request.method == 'POST':
        try:
            form = EmailListForm(request.POST)
                  

            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Email sent successfully'})
            else:
                return JsonResponse({'message': 'Failed to send email'}, status=400)

        except Exception as e:
            print(e)
            return JsonResponse({'message': f'Error: {str(e)}'}, status=500)

    return JsonResponse({'message': 'Invalid request method'}, status=400)




@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        # Extract data from the request
        #print(request.POST)
      
        name = request.POST.get('name')
        email = request.POST.get('email')
        m_subject = request.POST.get('subject')
        message = request.POST.get('message')


        try:
        
            message = Mail(
            from_email='smarticonsul@gmail.com',
            to_emails='smarticonsul@gmail.com',
            subject=f'{m_subject}',
            html_content=f'You have received a new message from your website contact form.\n\n"."Here are the details:\n\nName: {name}\n\n\nEmail: {email}\n\nSubject: {m_subject}\n\nMessage: {message}')
           
            

            #Send the email
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)

           # Check if the email was sent successfully
            if response.status_code == 202:
                return JsonResponse({'message': 'Email sent successfully'})
            else:
                return JsonResponse({'message': 'Failed to send email'}, status=response.status_code)

        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=500)

    return JsonResponse({'message': 'Invalid request method'}, status=400)



