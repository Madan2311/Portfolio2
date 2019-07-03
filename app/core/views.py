from django.shortcuts import render, HttpResponse, redirect
from django.core.exceptions import ObjectDoesNotExist
from perfil.forms import perfilForm
from perfil.models import perfil

# Create your views here.

def indexcore(request):
    return render(request, 'core/index.html')

def perfile(request):
    perfiles = perfil.objects.all()
    return render(request, 'core/listings.html',{'perfiles':perfiles})
    
def contactenos(request):
    return render(request, 'core/contact.html')

def EditPerfil(request):
    perfil_form = None
    error = None 
    try:
        Id = request.GET['Id']
        perfiles = perfil.objects.get(id = Id)
        if request.method == 'GET':
            perfil_form = perfilForm(instance = perfiles)
        else:
            perfil_form = perfilForm(request.POST, instance= perfiles)
            if perfil_form.is_valid():
                perfil_form.save()
            return redirect('perfil')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request, 'core/edit.html',{'perfil_form':perfil_form,'error':error})

def nuevoperfil(request):
    if request.method == 'POST':
        perfil_form = perfilForm(request.POST)
        if perfil_form.is_valid():
            perfil_form.save()
            return redirect('perfil')
    else:
        perfil_form = perfilForm()     
    return render(request, 'core/nuevoperfil.html',{'perfil_form':perfil_form})

def login(request):
    return render(request, 'core/login.html')

def registro(request):
    return render(request, 'core/register.html')

def nosotros(request):
    return render(request, 'core/about.html')

def EliminarPerfil(request):
    Id = request.GET['Id']
    perfiles = perfil.objects.get(id = Id)
    perfiles.delete()
    return redirect('perfil')    
    





