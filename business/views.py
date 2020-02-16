from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Jobapply


def show_business(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'services.html')


def port(request):
    return render(request, 'portfolio.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def showRegister(request):
    if request.method == 'POST':
        um = request.POST['um']
        email = request.POST['email']
        psw = request.POST['psw']
        user = User.objects.create_user(username=um, email=email, password=psw)
        user.save()

        return redirect('../business')

    return render(request, 'Register.html')


def showlogin(request):
    if request.method == 'POST':
        um = request.POST['um']
        psw = request.POST['psw']
        user = auth.authenticate(username=um, password=psw)
        if user is not None:
            auth.login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('../business')


def jobapply(request):
    if request.method == "POST":
        fn = request.POST.get('fn', '')
        ln = request.POST.get('ln', '')
        un = request.POST.get('un', '')
        ci = request.POST.get('ci', '')
        zi = request.POST.get('zi', '')
        app = Jobapply(fn=fn, ln=ln, un=un, ci=ci, zi=zi)
        app.save()
        print('pass')
    else:
        print('fail')
    return render(request, 'Jobapply.html')


