from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import render
from .forms import ParticipanteForm

# Create your views here.

from .forms import ParticipanteForm

from django.contrib import messages

# ...

def home(request):
    
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:obrigado')
        else:
            # Adicionar mensagens de erro ao contexto
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = ParticipanteForm()
    
    return render(request, 'core/index.html', {'form': form})




def obrigado(request):
    return render(request, 'core/obrigado.html')
