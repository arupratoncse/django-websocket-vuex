from django.shortcuts import render


def index(request, kanban_id):
    return render(request, 'kanban/index.html', {
        'kanban_id': kanban_id
    })
