from django.contrib import admin
from django.urls import path
from proyectoCloud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add/', views.add_tarea, name='add_tarea_form'),  
    path('edit/<int:tarea_id>/', views.edit_tarea, name='edit_tarea_form'),
    path('finalizar/<int:tarea_id>/', views.finalizar_tarea, name='finalizar_tarea'),
    path('tareas_finalizadas/', views.tareas_finalizadas, name='tareas_finalizadas'),
    path('eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'), 
]
