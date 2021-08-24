from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('programas', views.programas),
    path('programas/<int:programa_id>',views.displayprograma),
    path('programas/<int:programa_id>/editar',views.editar),
    path('programas/<int:programa_id>/update',views.actualizar),
    path('programas/nuevo',views.nuevo),
    path('programas/crear',views.crear),
    path('programas/<int:programa_id>/eliminar',views.eliminar)
]