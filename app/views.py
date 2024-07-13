
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redireciona para a página inicial após login bem-sucedido
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def task_list(request):
    return render(request, 'task.html')

def task_detail(request, task_id):
    # Adicione lógica para obter detalhes da tarefa
    return render(request, 'task_detail.html')
