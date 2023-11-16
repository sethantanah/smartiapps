from django.urls import path
from .views import home_page, file_preview, sort_files, download_file, send_email_with_attachment, send_mail, purchase, my_library
urlpatterns = [
    path('', home_page, name='index'),
    path('mylibrary/', my_library, name='mylibrary'),
    path(r'^purchase/(?P<pk>/d+)$', purchase, name='purchase'),
    path(r'^preview/(?P<pk>/d+)$', file_preview, name='preview'),
    path('sort-files/<str:sortby>/', sort_files, name='sort_files'),
    path(r'^download/(?P<pk>/d+)$', download_file, name='download'),
    path(r'^email/(?P<pk>/d+)$', send_email_with_attachment, name='email'),
    path('send-mail/', send_mail, name='send-mail'),
]
