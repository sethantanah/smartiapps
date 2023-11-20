import os
from io import BytesIO
import requests
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

from .formss import FileForm
from .models import FileTracker, Files, Purchases


def home_page(request, *args, **kwargs):
    request.session['location'] = 'home'
    empty_query = False
    shared = request.session.get('shared', False)
    download = request.session.get('download', False)
    if request.method == 'GET':
        files = Files.objects.all()
        query = ''

    if request.method == "POST":
        query = request.POST.get('q')
        if query:
            files = Files.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        else:

            if len(files) == 0:
                empty_query = True
            files = Files.objects.all()

    if shared:
        request.session['shared'] = False

    if download:
        request.session['download'] = False

    paginator = Paginator(files, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html',
                  {'files': page_obj, 'query': query, 'shared': shared, 'download': download,
                   'empty_query': empty_query, 'location': 'home'})


def my_library(request, *args, **kwargs):
    request.session['location'] = 'lib'
    empty_query = False
    if request.method == 'GET':
        files = Purchases.objects.all()
        query = ''

    if request.method == "POST":
        query = request.POST.get('q')
        if query:
            files = Purchases.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        else:

            if len(files) == 0:
                empty_query = True
            files = Purchases.objects.all()


    paginator = Paginator(files, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'mylibrary.html',
                  {'files': page_obj, 'query': query, 'empty_query': empty_query, 'location': 'lib'})

def sort_files(request, sortby):
    if request.method == 'GET':
        if sortby == 'all':
            files = Files.objects.all()
            paginator = Paginator(files, 3)
        else:
            files = Files.objects.filter(Q(file_type__icontains=sortby))
            paginator = Paginator(files, 10)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'index.html',
                      {'files': page_obj, 'query': '', 'shared': False, 'download': False,
                       'empty_query': False})



@login_required
def purchase(request, pk):
    request.session['selected_book_id'] = pk
    return redirect(reverse('initiate_payment'))

@login_required()
def file_preview(request, pk):
    
    try:
        # Case-insensitive search
        file = get_object_or_404(Files, pk=pk)
        # Check if the book is among the purchased books
        purchased_books = Purchases.objects.filter(book=file)
        exists = purchased_books.exists()

        if not exists:
              request.session['selected_book_id'] = pk
              return redirect(reverse('initiate_payment'))
        
        content_type = file.file_type
        file_type = content_type.split('/')[-1]

        if file_type == 'pdf':

        #     response = requests.get(file.file_url)
        #     file_content = response.content
        #     bytesIO = BytesIO(file_content)
        #    # print(blob_data)
        #     response = HttpResponse(file_content, content_type=content_type)
        #     response['Content-Disposition'] = f'inline; filename="{file.title}"'
            #print(file.file_url)


            return render(request, 'pdf_preview.html', context={'file_url':file.file_url,'response':'', 'pdf_content': '', 'title':file.title})

        else:
            return render(request, 'files-preview.html', {'file': file, 'type': file_type})
        
    except:
        request.session['selected_book_id'] = pk
        return redirect(reverse('initiate_payment'))
       
   


@login_required()
def download_file(request, pk):
    file = get_object_or_404(Files, pk=pk)
    content_type = file.file_type
    file_type = content_type.split('/')[-1]
    filename = f'{file.title}.{file_type}'

    try:
        tracker = file.filetracker
        downloads = tracker.downloads
        tracker.downloads = downloads + 1
        tracker.save()
    finally:
        pass

    response = requests.get(file.file_url)
    content = response.content
    headers = response.headers

    file_size = headers.get('Content-Length', 0)
    response = HttpResponse(content, content_type=content_type)
    response['Content-Disposition'] = f'attachment; filename={filename}'
    response['Content-Length'] = file_size
    request.session['downloaded'] = True
    return response


@login_required()
def send_mail(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pk = request.POST.get('pk')
       
        if email and pk:
            send_email_with_attachment(request, pk, email)
            return redirect(reverse('index'))
        else:
            return redirect(reverse('index'))


def send_email_with_attachment(request, pk, email):
    file = get_object_or_404(Files, pk=pk)
    content_type = file.file_type
    file_type = content_type.split('/')[-1]
    filename = f'{file.title}.{file_type}'
    my_mail = email
    email = EmailMessage(
        subject=f'Lizz-fileserver - {file.title}',
        body='Please find the attached file',
        from_email='sethsyd32@gmail.com',
        to=[my_mail],
    )
    # Open the file you want to attach
    response = requests.get(file.file_url)
    content = response.content
    # Add the file as an attachment to the email
    email.attach(filename, content, content_type)
    # Send the email
    email.send()
    try:
        tracker = file.filetracker
        emails = tracker.emails
        tracker.emails = emails + 1
        tracker.save()
    finally:
        pass
    request.session['shared'] = True
    #return redirect(reverse('index'))


def error_404_view(request, exception):
    # we add the path to the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')
