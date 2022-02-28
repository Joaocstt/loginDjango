from curses.ascii import US
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
def cadastro (request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
        
        
    else:
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        

        user = User.objects.filter(username=usuario).first()

        if user:
            return HttpResponse ('Já existe um usuário com esse usuername')
        
        user = User.objects.create_user(username=usuario, password=senha)
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso!')

        
def login (request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        usuario = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(username=usuario, password=senha)

        if user:
            login_django(request, user)
            return HttpResponse('Logado com sucesso!')
        else:
            return HttpResponse('usuário ou senha invalido')


def logout(request):
    logout(request)
    return HttpResponse('a')


@login_required(login_url="/login/")
def plataforma(request):
    return HttpResponse('Plataforma')