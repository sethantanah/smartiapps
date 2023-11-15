from django.contrib import admin

# Register your models here.
from .models  import  Payment, UserWallet

class  PaymentAdmin(admin.ModelAdmin):
    list_display  = ["id", "ref", 'amount', "verified", "date_created"]

admin.site.register(Payment, PaymentAdmin)
admin.site.register(UserWallet)