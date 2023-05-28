from django.urls import path
from . import views

urlpatterns = [
  
  	  path('',views.inicioApi,name='inicioApi' ),
      path('lista',views.listaUsuarios,name='listaUsuarios' ),
        
	]