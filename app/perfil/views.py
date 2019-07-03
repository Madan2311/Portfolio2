from django.shortcuts import render, HttpResponse

# Create your views here.

def perfil(request):
    return render(request, 'core/listings.html')
