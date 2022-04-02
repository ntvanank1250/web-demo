from django.urls import path
from . import views

app_name="main"
urlpatterns = [
    path('', views.home, name='home'),
    path('superadmin/', views.superadmin, name='superadmin'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('music/',views.music, name='music'),
    path('game', views.game, name='game'),
    path('gamesnake', views.gamesnake, name='gamesnake'),

]