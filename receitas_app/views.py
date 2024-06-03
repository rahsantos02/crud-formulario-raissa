from django.shortcuts import render, redirect
from receitas_app.forms import ReceitasForm
from receitas_app.models import Receitas


# Create your views here.

def home(request):
    data = {}
    data['db'] = Receitas.objects.all()
    return render(request, 'index2.html', data)

def cadastrar_receita(request):
    data = {}
    data['cadastrar_receita'] = ReceitasForm()
    return render(request, 'cadastrar_receita.html', data)

def create(request):
    form = ReceitasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request,pk):
    data = {}
    data['db'] = Receitas.objects.get(pk=pk)
    return render(request, 'index.html', data)

def minhas_receitas(request):
    return render(request,'minhas_receitas.html')

