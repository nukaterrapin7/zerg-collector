from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Zerg

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def zergs_index(request):
    zergs = Zerg.objects.all()
    return render(request, 'zergs/index.html', { 'zergs': zergs })

def zergs_detail(request, zerg_id):
    zerg = Zerg.objects.get(id=zerg_id)
    return render(request, 'zergs/detail.html', { 'zerg': zerg})

class ZergCreate(CreateView):
    model = Zerg
    fields = '__all__'

class ZergUpdate(UpdateView):
    model = Zerg
    fields = ['description', 'minerals', 'vespene']

class ZergDelete(DeleteView):
    model = Zerg
    success_url = '/zergs/'