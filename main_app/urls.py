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
    path('enemies/', views.EnemyList.as_view(), name='enemies_index'),
    path('zergs/<int:zerg_id>/assoc_enemy/<int:enemy_id>/', views.assoc_enemy, name='assoc_enemy'),
    path('enemies/<int:pk>/', views.EnemyDetail.as_view(), name='enemies_detail'),
    path('enemies/create/', views.EnemyCreate.as_view(), name='enemies_create'),
    path('enemies/<int:pk>/update/', views.EnemyUpdate.as_view(), name='enemies_update'),
    path('enemies/<int:pk>/delete/', views.EnemyDelete.as_view(), name='enemies_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('zergs/<int:zerg_id>/add_photo/', views.add_photo, name='add_photo'),
]