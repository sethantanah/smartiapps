from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('accounts.urls')),
                  path('library/', include('library.urls')),
                  path('dashboard/', include('dashboard.urls')),
                  path('payments/', include("payments.urls")),
                  path('dataexchange/', include("dataexchange.urls")),
                  path('', RedirectView.as_view(url='library/'))
              ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = 'library.views.error_404_view'
