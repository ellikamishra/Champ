from django.http import HttpResponse
from django.shortcuts import render,redirect, reverse
from django.contrib.auth import authenticate,login,logout
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
def register(request):
      if request.method == 'GET':
          return render(request, 'app/register.html')
      elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        is_student=request.POST.get('is_student')

        print(type(is_student))
        print(is_student)

        is_student=True if(is_student=='student') else False

        if username=="" or password=="":
            return render(request,'app/register.html')

        user=User.objects.create_user(username=username,password=password)
        userprofile=Profile(user=user,email=email,is_student=is_student)
        
        userprofile.save()
        login(request,user)
        return render(request, 'app/page.html')


def user_login(request):
    if request.method == 'GET':
        return render(request, 'app/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        if username == "" or password == "":
            return render(request, 'app/login.html')

        try:
            user = authenticate(username=username, password=password)
        except User.DoesnotExist:
            return render(request, 'app/login.html')

        user_prof = Profile.objects.get(user=user)
        if user.is_active:
            login(request, user)
            if user_prof.is_student:
                return render(request,'app/student.html')
            else:
                return render(request,'app/teacher.html')


def index(response):
    return render(response,'app/base.html',{})

def page(response):
    return render(response,'app/page.html',{})
