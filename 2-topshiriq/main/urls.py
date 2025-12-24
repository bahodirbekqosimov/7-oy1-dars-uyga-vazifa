from django.urls import path

from . import views


urlpatterns = [

    path("hello/",views.HelloView.as_view(),name="hello" ),
    path("greet/",views.GreetView.as_view(),name="greet" ),
    path("echo/",views.EchoView.as_view(), name='echo'),
    path("check-age/", views.Check_ageView.as_view(),name = 'check-age'),
    path("register/", views.RegisterView.as_view(), name = 'register'),
    path("square/<int:number>/", views.SquareView.as_view(), name='square'),
    
    

]