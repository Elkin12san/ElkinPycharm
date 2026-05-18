from django.shortcuts import render

from proyectos.models import Proyectos


# Create your views here.

def proyectos(request):
    proyecto = Proyectos.objects.all()
    return render(request, 'core/portfolio.html',{
        'proyecto': proyecto
    })