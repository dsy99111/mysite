from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,logout as auth_logout, authenticate
from django.contrib import messages



# Create your views here.
def home(request):
    post = Post.objects.all()[::-1]
    video = Video.objects.all()
    context = {'post' : post,'video' : video}
    return render(request,'home/index.html', context)
def contact(request):
    #return render(request,'home/contact.html')
    if request.method=='POST':
        name=request.POST['name']
        email = request.POST['email']
        msg = request.POST['comment']
        contact=Contact(name=name,email=email,message=msg)
        contact.save()

        #print(name,email,msg)
        return redirect('/contact')
    allpost = Contact.objects.all()[::-1]
    context = {'allpost': allpost}
    #print(allpost)
    return render(request,'home/contact.html',context)
def loginform(request):
    show = SignupForm()
    showl = LoginForm()
    context = {'showsignup': show,'showlogin':showl}
    return render(request,'home/loginform.html',context)
def signup(request):
    if request.method=='POST':
        fm=SignupForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            username = fm.cleaned_data['mobile']
            passw = fm.cleaned_data['password']
        myuser = User.objects.create_user(username,email,passw)
        myuser.first_name=name
        myuser.save()
        messages.success(request, "successfully created your account")
        return redirect("/loginform")
    return redirect('/')



def login(request):
    if request.method=='POST':
        fm=LoginForm(request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['mobile']
            passw=fm.cleaned_data['password']
        myuser=authenticate(username=username,password=passw)
        auth_login(request,myuser)
        messages.success(request,"Successfully logged in")
        return redirect("/")
    messages.error(request,"Something wrong")
    return redirect("/loginform")

def logout(request):
    auth_logout(request)
    messages.success(request,"Account log out")
    return redirect("/loginform")




