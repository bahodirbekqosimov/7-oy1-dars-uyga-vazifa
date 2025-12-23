from django.urls import path

from . import views


urlpatterns = [

    path("hello/",views.HelloView.as_view(),name="hello" ),
    path("greet/",views.GreetView.as_view(),name="greet" )
    
]