from django.shortcuts import render, redirect
from .models import Saidas
from .forms import NotaSaidasForm

def notaSaidaList(request):
    saida = Saidas.objects.all()
    template_name = 'notaSaidaList.html'
    context = {
        'saida': saida
    }
    return render(request, template_name, context)

def notaSaidaNew(request):
    if request.method == 'POST':
        form = NotaSaidasForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade - form.cleaned_data['quantidade']
            form.cleaned_data['produto'].preco = form.cleaned_data['preco']
            form.cleaned_data['produto'].save_base()
            form.save()
            return redirect('saida:notaSaidaList')
    else:
        form = NotaSaidasForm()
        template_name = 'notaSaidaNew.html'
        context = {
            'form': form,
        }
        return render(request, template_name, context)

def notaSaidaUpdate(request, pk):
    Saida = Saidas.objects.get(id=pk)
    quantidade_nota_antiga = Saida.quantidade
    if request.method == 'POST':
        form = NotaSaidasForm(request.POST, instance=Saida)
        if form.is_valid(): 
            form.save(commit=False)
            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade + quantidade_nota_antiga - form.cleaned_data['quantidade']
            form.cleaned_data['produto'].preco = form.cleaned_data['preco']
            form.cleaned_data['produto'].save_base()
            form.save()
            return redirect('saida:notaSaidaList')
    else:
        template_name = 'notaSaidaUpdate.html'
        context = {
            'form': NotaSaidasForm(instance=Saida),
            'pk': pk
        }
        return render(request, template_name, context)

def notaSaidaDelete(request, pk):
    Saida = Saidas.objects.get(id=pk)
    quantidade_nota_antiga = Saida.quantidade
    Saida.produto.quantidade = Saida.produto.quantidade + quantidade_nota_antiga 
    Saida.produto.save()
    Saida.delete()
    return redirect('saida:notaSaidaList')
