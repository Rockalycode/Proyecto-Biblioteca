from django.shortcuts import render, redirect, get_object_or_404
from .models import LibroPrestado
from .forms import LibroPrestadoForm

def lista_prestamos(request):
    prestamos = LibroPrestado.objects.all()
    
    if request.method == 'POST':
        form = LibroPrestadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_prestamos')
    else:
        form = LibroPrestadoForm()
        
    return render(request, 'ordenes/lista_prestamos.html', {'prestamos': prestamos, 'form': form})

def eliminar_prestamo(request, pk):
    prestamo = get_object_or_404(LibroPrestado, pk=pk)
    prestamo.delete()
    return redirect('lista_prestamos')