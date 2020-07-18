from django.contrib import admin
from .models import User_Details, Account_type


# Register your models here.
class User_DetailsAdmin(admin.ModelAdmin):
    list_display = ['user_id','user_name', 'user_phone', 'user_email', 'user_account_type']


class Account_typeAdmin(admin.ModelAdmin):
    list_display = ['account_type']


admin.site.register(User_Details, User_DetailsAdmin)
admin.site.register(Account_type, Account_typeAdmin)
