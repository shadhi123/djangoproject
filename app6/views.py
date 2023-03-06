from . forms import RegisterForm,LoginForm,UpdateForm,ChangePasswordForm,ImageForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout as logouts
from . models import Register,Images
# Create your views here.
def hello(request):
    return HttpResponse("<h1>welcome to django!</h1>")
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=Register.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,"email already exists")
                return redirect('/register')
            elif password!=confirmpassword:
                messages.warning(request,"password mismatched")
            else:
                tab=Register(Name=name,Age=age,Place=place,Email=email,Password=password) 
                tab.save()
                messages.success(request,"success")
                return redirect('/')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form}) 

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']

            user=Register.objects.get(Email=email)
            if not user:
                messages.warning(request,"email does not exists")
                return redirect('/login')
            elif password!=user.Password:
                messages.warning(request,"password incorrect")
            else:
                messages.success(request,"success")
                return redirect('/home/%s' % user.id)
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form}) 


def home(request,id):
    user=Register.objects.get(id=id)
    return render(request,'home.html',{'user':user})

def showusers(request):
    users=Register.objects.all()
    return render(request,'showusers.html',{'users':users}) 

def update(request,id):
    user=Register.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"success")
            return redirect('/showusers')
    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'form':form,'user':user})  

def delete(request,id):
    user=Register.objects.get(id=id)
    user.delete()
    messages.success(request,"deleted successfully")  
    return redirect('/showusers')

def changepassword(request,id):
    user=Register.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST or None)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            
            if oldpassword!=user.Password:
                messages.warning(request,"your old password is not correct")
                return redirect('/changepassword/%s' % user.id)
            elif newpassword==oldpassword:
                messages.warning(request,"old password is same as new password")
                return redirect('/changepassword/%s' % user.id)
            elif confirmpassword!=newpassword:
                messages.warning(request,"password is not correct")
                return redirect('/changepassword/%s' % user.id)
            else:
                messages.success(request,"password changed successfully")
                return redirect('/home/%s' % user.id)

    else:
        form=ChangePasswordForm()
    return render(request,'changepassword.html',{'form':form,'user':user})  

def logout(request):
    logouts(request)
    messages.success(request,'logged out successfully')
    return redirect('/')
            
def image(request):
    if request.method=='POST':
        form=ImageForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            photo=form.cleaned_data['Image']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=Images.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,"email already exists")
                return redirect('/image')
            elif password!=confirmpassword:
                messages.warning(request,"password mismatched")
            else:
                tab=Images(Name=name,Age=age,Place=place,Image=photo,Email=email,Password=password) 
                tab.save()
                messages.success(request,"success")
                return redirect('/')
    else:
        form=ImageForm()
    return render(request,'image.html',{'form':form}) 

def showimages(request):
    images=Images.objects.all()
    return render(request,'showimages.html',{'images':images}) 
              
                
            






            


            


            
            
        
     
             

