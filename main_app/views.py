from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Enemy, Zerg, Enemy, Photo
from .forms import EssenceForm
import uuid
import boto3
import os


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def zergs_index(request):
    zergs = Zerg.objects.filter(user=request.user)
    return render(request, 'zergs/index.html', { 'zergs': zergs })

@login_required
def zergs_detail(request, zerg_id):
    zerg = Zerg.objects.get(id=zerg_id)
    id_list = zerg.enemies.all().values_list('id')
    enemis_zerg_doesnt_have = Enemy.objects.exclude(id__in=id_list)
    essence_form = EssenceForm()
    return render(request, 'zergs/detail.html', {
        'zerg': zerg, 'essence_form': essence_form,
        'enemies': enemis_zerg_doesnt_have
    })

@login_required
def add_essence(request, zerg_id):
  form = EssenceForm(request.POST)
  if form.is_valid():
    new_essence = form.save(commit=False)
    new_essence.zerg_id = zerg_id
    new_essence.save()
  return redirect('detail', zerg_id=zerg_id)

@login_required
def assoc_enemy(request, zerg_id, enemy_id):
  Zerg.objects.get(id=zerg_id).enemies.add(enemy_id)
  return redirect('detail', zerg_id=zerg_id)

class EnemyList(LoginRequiredMixin, ListView):
  model = Enemy

class EnemyDetail(LoginRequiredMixin, DetailView):
  model = Enemy

class EnemyCreate(LoginRequiredMixin, CreateView):
  model = Enemy
  fields = '__all__'

class EnemyUpdate(LoginRequiredMixin, UpdateView):
  model = Enemy
  fields = ['name', 'color']

class EnemyDelete(LoginRequiredMixin, DeleteView):
  model = Enemy
  success_url = '/enemies/'

class ZergCreate(LoginRequiredMixin, CreateView):
    model = Zerg
    fields = ['name', 'description', 'minerals', 'vespene']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ZergUpdate(LoginRequiredMixin, UpdateView):
    model = Zerg
    fields = ['description', 'minerals', 'vespene']

class ZergDelete(LoginRequiredMixin, DeleteView):
    model = Zerg
    success_url = '/zergs/'

def add_photo(request, zerg_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, zerg_id=zerg_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', zerg_id=zerg_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)