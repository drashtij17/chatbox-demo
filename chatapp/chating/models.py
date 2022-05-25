from django.db import models
from app.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.



class ChatModel(models.Model):
    sender = models.CharField(max_length=100, default=None)
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=40)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

class Contact(models.Model):
    name = models.CharField(max_length=50, default=None)
    mobile = PhoneNumberField( null = True, blank = True)
    loginuser = models.ForeignKey(User,on_delete=models.CASCADE)