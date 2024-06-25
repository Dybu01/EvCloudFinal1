from django.shortcuts import render, redirect, get_object_or_404
from proyectoCloud.models import Tareas, TareasFinalizadas
from proyectoCloud.forms import TareaForm
from datetime import date, timedelta
from django.db.models import Case, When, IntegerField

# Create your views here.
def index(req):
    today = date.today()
    limite = today + timedelta(days=3)

    tareas_por_expirar = Tareas.objects.filter(fecha_termino__lte=limite, finalizada=False).annotate(
        prioridad_valor=Case(
            When(prioridad='Alta', then=1),
            When(prioridad='Media', then=2),
            When(prioridad='Baja', then=3),
            default=4,
            output_field=IntegerField()
        )
    ).order_by('prioridad_valor', 'fecha_termino')

    tareas = Tareas.objects.filter(finalizada=False).annotate(
        prioridad_valor=Case(
            When(prioridad='Alta', then=1),
            When(prioridad='Media', then=2),
            When(prioridad='Baja', then=3),
            default=4,
            output_field=IntegerField()
        )
    ).order_by('prioridad_valor', 'fecha_termino')
    
    tareas_finalizadas = Tareas.objects.filter(finalizada=True)

    context = {
        'tareas': tareas,
        'tareas_por_expirar': tareas_por_expirar,
        'tareas_finalizadas': tareas_finalizadas
    }
    return render(req, 'index.html', context)


# Vista para manejar el formulario de adición de tareas
def add_tarea(req):
    if req.method == 'POST':
        form = TareaForm(req.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            fecha_inicio = form.cleaned_data.get('fecha_inicio')
            fecha_termino = form.cleaned_data.get('fecha_termino')
            if fecha_inicio >= fecha_termino:
                return render(req, 'addTarea.html', {'form': form, 'error_message': 'La fecha de inicio debe ser anterior a la fecha de término'})
            tarea.save()
            return redirect('index')
    else:
        form = TareaForm()
    return render(req, 'addTarea.html', {'form': form})

# Vista para editar una tarea
def edit_tarea(req, tarea_id):
    tarea = get_object_or_404(Tareas, pk=tarea_id)
    if req.method == 'POST':
        form = TareaForm(req.POST, instance=tarea)
        if form.is_valid():
            tarea = form.save(commit=False)
            fecha_inicio = form.cleaned_data.get('fecha_inicio')
            fecha_termino = form.cleaned_data.get('fecha_termino')
            if fecha_inicio >= fecha_termino:
                return render(req, 'editTarea.html', {'form': form, 'tarea': tarea, 'error_message': 'La fecha de inicio debe ser anterior a la fecha de término'})
            tarea.save()
            return redirect('index')
    else:
        form = TareaForm(instance=tarea)
    return render(req, 'editTarea.html', {'form': form, 'tarea': tarea})

def finalizar_tarea(req, tarea_id):
    tarea = get_object_or_404(Tareas, pk=tarea_id)
    tarea.delete()
    return redirect('index')


def tareas_finalizadas(req):
    tareas_finalizadas = TareasFinalizadas.objects.all()
    tareas_eliminadas = Tareas.objects.filter(finalizada=True)  # Obtener todas las tareas eliminadas
    return render(req, 'tareas_finalizadas.html', {'tareas_finalizadas': tareas_finalizadas, 'tareas_eliminadas': tareas_eliminadas})


def eliminar_tarea(req, tarea_id):
    tareas = Tareas.objects.get(id=tarea_id)
    tareas.finalizada = True  # Marcar la tarea como finalizada en lugar de eliminarla
    tareas.save()
    return redirect('listar_tareas')

def listar_tareas(req):
    tareas = Tareas.objects.filter(finalizada=False)  # Obtener todas las tareas que no estén finalizadas
    tareas_eliminadas = Tareas.objects.filter(finalizada=True)  # Obtener todas las tareas eliminadas
    return render(req, 'index.html', {'tareas': tareas, 'tareas_eliminadas': tareas_eliminadas})

