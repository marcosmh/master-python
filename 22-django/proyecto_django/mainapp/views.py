from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from mainapp.forms import RegisterForm



# Create your views here.

def index(request):
    return render(request,'mainapp/index.html',{
        'title': 'inicio'
    })

def about(request):
    return render(request,'mainapp/about.html',{
        'title': 'Acerca de mi'
    })

def register_page(request):
    
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        register_form = RegisterForm(request.POST)
        if request.method == "POST":
            
            if register_form.is_valid():
                register_form.save()
                messages.success(request,'Usuario se ha guardado correctamente.')

                return redirect('inicio')

        return render(request,'users/register.html',{
            'title': 'Registro',
            'register_form': register_form
        })

def login_page(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            print("user:" , user)

            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.warning(request,'Usuario No Valido ó Contraseña Incorrecta')

        return render(request,'users/login.html',{
            'title': 'Iniciar Sesión'
        })

def logout_page(request):
    logout(request)
    return redirect('login')