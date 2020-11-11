from django.shortcuts import render
from django.contrib import messages
from .forms import KanbanForm
from .models import Kanban
from django.shortcuts import redirect


def home(request):
    if request.method == 'POST':
        kanban_form = KanbanForm(request.POST)
        if kanban_form.is_valid():
            post = kanban_form.save(commit=False)
            post.save()
            messages.success(request, "New kanban created")
        else:
            messages.warning(request, "Kanban creation Failed")
    form = KanbanForm(None)
    all_kanban = Kanban.objects.all()
    return render(request, 'kanban/index.html', {'form': form, 'kanbans': all_kanban})


def kanban_detail(request, kanban_id):
    try:
        Kanban.objects.get(id=kanban_id)
    except Kanban.DoesNotExist:
        return redirect('kanban')

    return render(request, 'kanban/detail.html', {
        'kanban_id': kanban_id
    })


def delete_kanban(request, kanban_id):
    try:
        Kanban.objects.get(id=kanban_id).delete()
        messages.success(request, "Kanban deleted successfully!")
    except Exception:
        messages.warning(request, "Kanban deletion Failed!")
    return redirect('kanban')
