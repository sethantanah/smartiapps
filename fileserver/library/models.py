from django.db import models
from django.shortcuts import reverse
import os
from django.conf import settings


def upload_to(instance, filename):
    if instance.file_type == 'audio':
        return os.path.join('media/', filename)
    else:
        pass


class Files(models.Model):
    title = models.CharField(max_length=255, help_text='title', blank=False)
    description = models.CharField(max_length=10000, help_text='description', blank=True)
    file_url = models.CharField(max_length=255, help_text='url', blank=True)
    file = models.FileField(help_text='file', blank=True, upload_to='files/')
    preview_image = models.FileField(help_text='file', blank=True, upload_to='images/')
    file_preview = models.CharField(max_length=255, help_text='url', blank=True)
    file_type = models.CharField(max_length=2500, help_text='', blank=True)
    published = models.DateTimeField(auto_now_add=True, blank=True)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return self.title

    def get_file_type(self):
        return str(self.file_type.split('/')[-1])

    def get_absolute_url(self):
        return reverse('preview', args=[str(self.id)])
    
    def get_purchase_url(self):
        return reverse('purchase', args=[str(self.id)])

    def get_download_url(self):
        return reverse('download', args=[str(self.id)])

    def get_email_url(self):
        return reverse('email', args=[str(self.id)])

    def select_file_url(self):
        return reverse('email', args=[str(self.id)])

    def get_update_url(self):
        return reverse('update_file', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('delete_file', args=[str(self.id)])
    
    def get_confirm_delete_url(self):
        return reverse('confirm_delete_file', args=[str(self.id)])
    
    def get_add_to_cart_url(self):
         return reverse("add-to-cart", kwargs={'slug':self.slug})
    
    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={'slug': self.slug})

    
class FileTracker(models.Model):
    file = models.OneToOneField(Files, on_delete=models.CASCADE)
    downloads = models.IntegerField(default=0)
    emails = models.IntegerField(default=0)

    def __str__(self):
        return self.file.title
    



class Purchases(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Files, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
  




