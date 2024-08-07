from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth


# Create your views here.

def userRegistration(request):

    if request.method=='POST':

        username=request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword = request.POST.get('password1')

        if password==cpassword:

            if User.objects.filter(username=username).exists():
                messages.info(request,'This username is already exists')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,'This email is already exists')
                return redirect('register')
            
            else:
                user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                messages.success(request,'Your registration successful !!!')
                return redirect('/')

    return render(request,'account/register.html')

def loginPage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user= auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('list_view')

        else:
            messages.error(request,'Invalid username or password')
            return redirect('/')

    return render(request, 'account/login.html')

def logoutView(request):
    auth.logout(request)
    return redirect('/')
                    
