from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin

admin.site.register(User,UserAdmin)

UserAdmin.fieldsets += ("custom fields set",{'fields':('statuss','phoneNumber')}),
list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'is_teacher', 'is_student', 'mailing_address'
        )


