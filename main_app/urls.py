from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('zergs/', views.zergs_index, name='index'),
    path('zergs/<int:zerg_id>/', views.zergs_detail, name='detail'),
]