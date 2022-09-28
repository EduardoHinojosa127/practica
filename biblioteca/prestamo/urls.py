from django.urls import path

from . import views

app_name = 'prestamo'

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:libro_id>/', views.detalle, name='detalle'),
    path('<int:libro_id>/prestar', views.prestar, name='prestar')
]