from django.urls import path
from . import views

app_name="main"
urlpatterns = [
    path('', views.home, name='home'),
    path('changepass/', views.changepass, name='changepass'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('music/',views.music, name='music'),
    path('game', views.game, name='game'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blog_i, name='blog_i'),
    path('blog/add_blog/', views.add_blog, name='add_blog'),

]