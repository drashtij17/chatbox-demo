
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate 
from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
User = get_user_model()
# Create your views here.


def register(request):
    if request.method =="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')      
    
        user = User.objects.create_user(username=username,email=email,password=password)
        user.set_password(password)
        user.save()
        if user:
            
            return redirect('login')
        else:
            return render(request,'app/register.html')

        print(user,"???")
    return render(request,'app/register.html')



def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        request.session['username'] = username
        if user is not None:
            request.session['username'] = username
            auth.login(request,user)                  
            return redirect("index")
    return render(request,'app/login.html')    

def logout(request):
    try:
        print(request.session['username'])
        del request.session['username']
        return redirect('login')
        # return render(request,'school/login.html')
    except KeyError:
        pass
    return 0