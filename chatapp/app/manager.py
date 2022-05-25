from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password



class BaseAccountManager(BaseUserManager):

    def create(self,password=None,is_superuser=False,**kwargs):
        print("create was code")
        # kwargs.setdefault('is_staff' , is_staff)
        kwargs.setdefault('is_superuser' , is_superuser)
        # kwargs.setdefault('name' , name)
        # if  not email:
        #     raise ValueError('enater valid email address')
        
          
        account = self.model(**kwargs)
        print("hello ",make_password(password))
        print("passwordd ",password)
        account.password=make_password(password)

        account.save()

        return account 
        
    def create_staffuser(self,password=None,**kwargs):  ### this isfail function
        print("create stafff")
      
        # if  not email:
        #     raise ValueError('enater valid email address')
        
          
        account = self.model(**kwargs)
        print("hello ",make_password(password))
        print("passwordd ",password)
        account.password=make_password(password)

        account.save()

        return account    

    def create_superuser(self, password, **extra_fields):
    #   print(email)  
      extra_fields.setdefault('is_admin' , True)
      extra_fields.setdefault('is_staff' , True)
      extra_fields.setdefault('is_superuser' , True)
    #   extra_fields.setdefault('' , True)
      return self.create( password, **extra_fields)

       
          