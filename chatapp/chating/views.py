from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from .models import ChatModel,Contact
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.

import datetime

User = get_user_model()

@login_required
def index(request):
    if request.session.has_key('username'):
        Username = request.session['username']
        getid = User.objects.get(username=Username).id
        print(getid,"KKKKKKKKK")

        print(request.user.username, "@@@@")
        users = User.objects.exclude(username=request.user.username)

        savedname = Contact.objects.filter(loginuser=getid)
        print(savedname,"^^^^^^^^^^^^^^^^^^^^^")
        return render(request, 'chating/index.html',context={'users': users,'show':savedname})
    else:
        return redirect("/")
@login_required
def chatPage(request,username):
    if request.session.has_key('username'):
        Username = request.session['username']
        getid = User.objects.get(username=Username).id
        # print(getid,"KKKKKKKKK")
        user_obj = User.objects.get(username=username)
        users = User.objects.exclude(username=request.user.username)
        print(request.user, "===", user_obj.id)

        if request.user.id > user_obj.id:
            thread_name = f'chat_{request.user.id}-{user_obj.id}'
            print(thread_name,"????")
        else:
            thread_name = f'chat_{user_obj.id}-{request.user.id}'

        message_objs = ChatModel.objects.filter(thread_name=thread_name)

        savedname = Contact.objects.filter(loginuser=getid)
       
        return render(request, 'chating/chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs,"show":savedname})
    else:
        return redirect("/")

def contact(request):
    # phonenumber in registration and mobile in contact table
    if request.session.has_key('username'):
        Username = request.session['username']
        getid = User.objects.get(username=Username)
        print(getid,"777777777777")
        if request.method =="POST":
            name = request.POST.get('name')
            print(name,"#$%#$%#$")
            mobile = request.POST.get('contact')
           
            # verify = User.objects.filter(phoneNumber=mobile)
            # print(verify,"))")
            # if verify:
            addnumber = Contact.objects.create(name=name,mobile=mobile,loginuser=getid)
            addnumber.save()
            return redirect("index")
            # else:
            #     return HttpResponse("no")
            # savenumber = Contact.objects.create_user(name=name,mobile=mobile)
        return render(request,'chating/contact.html',{"Username":Username})
    else:
        return redirect("/")
