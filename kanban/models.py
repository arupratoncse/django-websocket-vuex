from django.db import models


class Kanban(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Kanban({}:{})'.format(self.id, self.title)

    @classmethod
    def get_by_id(cls, kanban_id):
        return cls.objects.get(pk=kanban_id)

    @classmethod
    def get_or_create(cls, kanban_id):
        try:
            return cls.get_by_id(kanban_id)
        except Exception:
            return Kanban.objects.create(
                title='new'
            )


class PipeLine(models.Model):

    kanban = models.ForeignKey('Kanban', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'PipeLine({}:{} belonged {}) '.format(self.id, self.title, self.kanban)

    @property
    def cards(self):
        cards = self.card_set.order_by('order')
        return cards

    @property
    def json(self):
        return {
            'id': self.id,
            'title': self.title,
        }

    @classmethod
    def create(cls, **params):
        return cls.objects.create(**params)

    @classmethod
    def get_list_by_kanban_id(cls, kanban_id):
        return cls.objects.filter(kanban_id=kanban_id).order_by('order')


class Card(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    order = models.IntegerField()
    pipeline = models.ForeignKey('PipeLine', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Card({}:{} belonged {}) '.format(self.id, self.title, self.pipeline)

    @property
    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
        }

    @classmethod
    def create(cls, **params):
        return cls.objects.create(**params)

    @classmethod
    def get_by_id(cls, card_id):
        return cls.objects.get(pk=card_id)
