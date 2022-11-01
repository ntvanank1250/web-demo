from django.urls import path
from . import views

app_name="main"
urlpatterns = [
    path('', views.home, name='home'),
    path('changepass/', views.changepass, name='changepass'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),

    path('order/', views.order, name='order'),
    path('paypal/', views.paypal, name='paypal'),

    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blog_i, name='blog_i'),
    path('blog/add_blog/', views.add_blog, name='add_blog'),
    

]