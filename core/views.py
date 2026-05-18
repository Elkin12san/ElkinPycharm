from django.shortcuts import render
from django.views.generic import ListView

from core.models import *


# Create your views here.


class AllToDos(ListView):
    model = ToDoItem
    template_name = "core/index.html"


def index(request):
    return render(request, 'core/index.html')
def about(request):
    return render(request, 'core/about.html')
def contact(request):
    persona = Personas.objects.all()
    return render(request, 'core/contact.html', {
        'persona':persona
    })