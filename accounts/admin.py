
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, EmailVerification

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    ordering = ['email'] 

admin.site.register(CustomUser, CustomUserAdmin)


class EmailVerificationAdmin(admin.ModelAdmin):
    list_display =['id', 'user','token']

admin.site.register(EmailVerification, EmailVerificationAdmin)