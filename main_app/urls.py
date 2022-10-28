from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('zergs/', views.zergs_index, name='index'),
    path('zergs/<int:zerg_id>/', views.zergs_detail, name='detail'),
    path('zergs/create/', views.ZergCreate.as_view(), name='zergs_create'),
    path('zergs/<int:pk>/update/', views.ZergUpdate.as_view(), name='zergs_update'),
    path('zergs/<int:pk>/delete/', views.ZergDelete.as_view(), name='zergs_delete'),
    path('zergs/<int:zerg_id>/add_essence/', views.add_essence, name='add_essence'),
]