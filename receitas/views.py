from django.shortcuts import render
from .models import Receita


# Create your views here.
def index(request):

    # pip install pylint-django para sumir o erro de Receita
    receitas = Receita.objects.all()

    dados = {
        'receitas' : receitas
    }

    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')
