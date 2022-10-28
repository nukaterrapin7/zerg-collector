from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Zerg
from .forms import EssenceForm

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
    essence_form = EssenceForm()
    return render(request, 'zergs/detail.html', {
        'zerg': zerg, 'essence_form': essence_form
    })

def add_essence(request, zerg_id):
  form = EssenceForm(request.POST)
  if form.is_valid():
    new_essence = form.save(commit=False)
    new_essence.zerg_id = zerg_id
    new_essence.save()
  return redirect('detail', zerg_id=zerg_id)


class ZergCreate(CreateView):
    model = Zerg
    fields = '__all__'

class ZergUpdate(UpdateView):
    model = Zerg
    fields = ['description', 'minerals', 'vespene']

class ZergDelete(DeleteView):
    model = Zerg
    success_url = '/zergs/'