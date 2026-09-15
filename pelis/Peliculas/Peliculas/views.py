from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Q
from .models import Pelicula, Distribuidora

# 1. Catálogo Principal
def catalogo_view(request):
    peliculas = Pelicula.objects.all()
    
    total_copias = Pelicula.objects.aggregate(Sum('cantidad'))['cantidad__sum'] or 0
    sin_copias = Pelicula.objects.filter(Q(estado='agotado') | Q(cantidad=0)).count()
    generos_count = Pelicula.objects.values('categoria').distinct().count()

    context = {
        'peliculas': peliculas,
        'total_copias': total_copias,
        'sin_copias': sin_copias,
        'generos_count': generos_count,
    }
    return render(request, 'Peliculas/base.html', context)

# 2. Ingresar Película
def ingresar_pelicula_view(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria')
        cantidad = int(request.POST.get('cantidad', 0))
        precio = int(request.POST.get('precio', 0))

        Pelicula.objects.create(
            codigo=codigo,
            nombre=nombre,
            categoria=categoria,
            cantidad=cantidad,
            precio=precio,
            estado='disponible' if cantidad > 0 else 'agotado'
        )
        return redirect('catalogo')

    return render(request, 'Peliculas/ingresar.html')

# 3. Alertas de Stock
def alertas_stock_view(request):
    peliculas_agotadas = Pelicula.objects.filter(Q(estado='agotado') | Q(cantidad=0))
    return render(request, 'Peliculas/alerta_stock.html', {'peliculas': peliculas_agotadas})

# 4. Distribuidoras
def distribuidoras_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('empresa')
        rubro = request.POST.get('rubro')
        telefono = request.POST.get('telefono')
        
        Distribuidora.objects.create(nombre=nombre, rubro=rubro, telefono=telefono)
        return redirect('distribuidoras')

    distribuidoras = Distribuidora.objects.all()
    return render(request, 'Peliculas/proveedores.html', {'distribuidoras': distribuidoras})

# 5. Eliminar Película
def eliminar_pelicula_view(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    pelicula.delete()
    return redirect('catalogo')