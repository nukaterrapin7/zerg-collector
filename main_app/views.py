from django.shortcuts import render
from .models import Zerg

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def zergs_index(request):
    zergs = Zerg.objects.all()
    return render(request, 'zergs/index.html', { 'zergs': zergs })