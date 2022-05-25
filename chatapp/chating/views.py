from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from .models import ChatModel
from django.contrib.auth.decorators import login_required
# Create your views here.

import datetime

User = get_user_model()

@login_required
def index(request):
    print(request.user.username, "@@@@")
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chating/index.html',context={'users': users})


@login_required
def chatPage(request,username):
    if request.session.has_key('username'):
        Username = request.session['username']
        current_datetime = datetime.datetime.now()  
        user_obj = User.objects.get(username=username)

        print(user_obj,"?????????????????????????????????")

        users = User.objects.exclude(username=request.user.username)
        print(request.user, "===", user_obj.id)

        if request.user.id > user_obj.id:
            thread_name = f'chat_{request.user.id}-{user_obj.id}'
            print(thread_name,"????")
        else:
            thread_name = f'chat_{user_obj.id}-{request.user.id}'

        message_objs = ChatModel.objects.filter(thread_name=thread_name)

        print(message_objs,"???????????????")

        return render(request, 'chating/chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs,"current_datetime":current_datetime})
    else:
        return redirect("/")



