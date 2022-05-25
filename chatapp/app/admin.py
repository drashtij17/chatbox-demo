from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin

admin.site.register(User,UserAdmin)

UserAdmin.fieldsets += ("custom fields set",{'fields':('statuss','phoneNumber')}),



