from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from  Webapp.models import register,BuilD_Profile
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
from Webapp.form import ImageForm
from Webapp.models import Image
import requests



def Login_Just(request):
    return render(request,'MyApp/login.html')

def Base(request):
    return render(request,'MyApp/base.html')


def Registration(request):
    return render(request,'MyApp/registration.html')

def Login(request):
    if request.POST:
        email= request.POST.get('email')
        password = request.POST.get('password')
        count = register.objects.filter(email=email,password=password)
        if count.count()>0:
            request.session['useremail'] = email
            return redirect('build')
        else:
            return render(request,"MyApp/login.html",{'message':'Invalid User or Password'})


def SaveRegister(request):
    firstname = request.POST.get("firstname")
    email = request.POST.get("email")
    password = request.POST.get("password")
    auth=register.objects.filter(email=email).count()
    if auth>0:
        message="User Already Registered With This User"
        return render(request, "MyApp/registration.html", {'message': message})
    else:
        register(firstname=firstname, email=email, password=password).save()
    return redirect('build')


def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "MyApp/profile.html", {"obj": obj})
    else:
        form = ImageForm()
    img = Image.objects.all()
    return render(request, "MyApp/profile.html", {"img": img, "form": form})

def Build_Ur_Profile(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    image = request.FILES.get("Image")
    age = request.POST.get("age")
    DOB = request.POST.get("DOB")
    shown = BuilD_Profile.objects.filter(email=email)
    if shown.count()>0:
        return render(request, "MyApp/buildurprofile.html", {})
    else:
        BuilD_Profile(name=name, email=email, image=image, age=age, DOB=DOB).save()
    return redirect('profile')

def Profile(request):
   show = BuilD_Profile.objects.all()
   context = {'show':show}
   return render(request, 'MyApp/profile.html',context)



def Logout(request):
    request.session.flush()
    return redirect("/")


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

