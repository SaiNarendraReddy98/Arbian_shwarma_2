from django.shortcuts import render
from app.forms import *
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def dummy(request):
    if request.session.get('username'):
        username = request.session.get('username')
        d = {'username':username}
        return render(request,'dummy.html',d)
    return render(request,'dummy.html')




def registration(request):
    UFO = UserForm()
    PFO = ProfileForm()
    d = {'UFO':UFO,'PFO':PFO}
    if request.method == 'POST' and request.FILES:
        UFD = UserForm(request.POST)
        PFD = ProfileForm(request.POST,request.FILES)
        if UFD.is_valid and PFD.is_valid():
            MUFDO = UFD.save(commit=False)
            pw = UFD.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO = PFD.save(commit=False)
            MPFDO.username = MUFDO
            MPFDO.save()

            send_mail('Registraion Successful','Welcom to Arabian Shawarma you have successfully register',
            'sainarendra62645@gmail.com',
            [MUFDO.email],
            fail_silently = False,)

            return HttpResponse('<center><h1>Registration successfully')
        else:
            return HttpResponse('<center><h1>Invalid data')
        
    return render(request,'registration.html',d)



def user_login(request):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        AUO = authenticate(username=un,password=pw)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username'] = un
            return HttpResponseRedirect(reverse('dummy'))
        else:
            return HttpResponse('<center><h1>Invalid credentials please try again...')
        
    return render(request,'user_login.html')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('dummy'))
