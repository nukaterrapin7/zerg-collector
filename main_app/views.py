from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Zerg:
    def __init__(self, name, description, minerals, vespene):
        self.name = name
        self.description = description
        self.minerals = minerals
        self.vespene = vespene

zergs = [
    Zerg('Zergling', 'Small melee unit.', 50, 0),
    Zerg('Roach', 'Small range unit', 75, 25),
    Zerg('Ultralisk', 'Large melee unit', 300, 200)
]

def home(request):
    return HttpResponse('<h1>Welcome to The Swarm</h1>')

def about(request):
    return render(request, 'about.html')

def zergs_index(request):
    return render(request, 'zergs/index.html', { 'zergs': zergs})