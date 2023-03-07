from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

    

def logout(request):
    auth.logout(request)
    return redirect('test')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
            
        if user is not None:
                auth.login(request,user)
                messages.info(request, 'Logged In...')
                return redirect("test")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'The Username has been taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'The email exists in the Database already')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,  password=password1, email=email)
                user.save()
                messages.info(request, 'User created. Please Login to Continue...')
                return redirect('index')
        else:
            print("The Passwords are not matching")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')    


