from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout, login
#flash up messages
from django.contrib import messages

# Create your views here.
def home(request):
    #check to see if user is login in or not
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        #Authenticate user
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,('You have been logged in'))
            return redirect('home')
        else:
            messages.success(request,('Error logging in - Please try again'))
            return redirect('home')
    else:
        return render(request,'home.html',{})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,('You have been logged out'))
    return redirect('home')
    
