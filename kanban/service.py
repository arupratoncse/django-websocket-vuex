from .models import Kanban, PipeLine, Card
from channels.db import database_sync_to_async


@database_sync_to_async
def get_whole_json(kanban_id):
    kanban = Kanban.get_or_create(kanban_id)
    pipeline_list = PipeLine.get_list_by_kanban_id(kanban.id)
    result = []
    for pipeline in pipeline_list:
        result.append({
            'id': pipeline.id,
            'title': pipeline.title,
            'cards': [card.json for card in pipeline.cards]
        })

    return result


@database_sync_to_async
def update_kanban(pipeline_id, card_id_list):
    """
    Update cards in the pipeline
    :return:
    """
    print('update_kanban')
    order = 0
    for card_id in card_id_list:
        card = Card.get_by_id(card_id=card_id)
        card.order = order
        card.pipeline_id = pipeline_id
        card.save()
        order += 1
        print(card)


@database_sync_to_async
def add_card(pipeline_id, title, content, order):
    Card.create(
        pipeline_id=pipeline_id,
        title=title,
        content=content,
        order=order,
    )


@database_sync_to_async
def update_card(card_id, title, content):
    Card.objects.filter(id=card_id).update(title=title, content=content)


@database_sync_to_async
def delete_card(card_id):
    Card.objects.filter(id=card_id).delete()


@database_sync_to_async
def add_pipeline(kanban_id, title, order):
    PipeLine.create(
        kanban_id=kanban_id,
        title=title,
        order=order,
    )


@database_sync_to_async
def update_pipeline(pipeline_id, title):
    PipeLine.objects.filter(id=pipeline_id).update(title=title)


@database_sync_to_async
def delete_pipeline(pipeline_id):
    PipeLine.objects.filter(id=pipeline_id).delete()
