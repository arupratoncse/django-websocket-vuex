from .models import Kanban
from django.forms import ModelForm


class KanbanForm(ModelForm):
    class Meta:
        model = Kanban
        fields = ["title"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # bootstrap対応
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control mr-sm-2'
        self.fields['title'].widget.attrs['placeholder'] = "Kanban Name"
