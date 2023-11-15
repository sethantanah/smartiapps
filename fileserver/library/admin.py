from django.contrib import admin

from .models import Files, FileTracker, Purchases

admin.site.register(Files)
admin.site.register(FileTracker)
admin.site.register(Purchases)
