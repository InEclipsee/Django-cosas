from django.shortcuts import render
from core.models import Residencia
from core.models import Correspondencia


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def residences(request):
    dataRes = Residencia.objects.all()
    context = {'data': dataRes}
    return render(request, 'core/residencias.html', context)

def correspondances(request):
    dataCor = Correspondencia.objects.all()
    context = {'data': dataCor}
    return render(request, 'core/correspondencias.html', context)
