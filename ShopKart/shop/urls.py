from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('home', views.home,name="home"),
    path('login', views.login_page,name="login"),
    path('logout', views.log_out,name="logout"),
    path("register", views.register,name="register"),
    path("Collections", views.Collections,name="Collections"),
    path("Collections/<str:name>", views.Collectionview,name="Collections"),
    path("Collections/<str:cname>/<str:pname>", views.product_details ,name="product_details"),
    
]

