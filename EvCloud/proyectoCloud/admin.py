from django.contrib import admin
from proyectoCloud.models import Tareas

class TareasAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_inicio', 'fecha_termino', 'prioridad']
admin.site.register(Tareas, TareasAdmin)