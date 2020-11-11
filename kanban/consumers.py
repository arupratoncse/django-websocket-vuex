import json

from channels.generic.websocket import AsyncWebsocketConsumer
from . import service as kanban_sv


class KanbanConsumer(AsyncWebsocketConsumer):
    """
    WebSocket communication handler (asynchronous implementation)
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type_map = {
            'update': self._update,
            'add_card': self._add_card,
            'add_pipeline': self._add_pipeline,
        }

    async def connect(self):
        self.kanban_id = self.scope['url_route']['kwargs']['kanban_id']
        self.kanban_name = 'kanban_{}'.format(self.kanban_id)

        # Join room group
        await self.channel_layer.group_add(
            self.kanban_name,
            self.channel_name
        )

        await self.accept()
        # Initial data
        await self.send(text_data=json.dumps({
            'kanban': await kanban_sv.get_whole_json(self.kanban_id),
            'type': 'set_data',
        }))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.kanban_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message_type = text_data_json['type']
        payload = text_data_json['payload']
        # Dispatch to processing according to type
        await self.type_map[message_type](payload)

    # Receive message from room group
    async def updated(self, event):
        payload = event['payload']
        # I will update everything once
        await self.send(text_data=json.dumps({
            'type': 'set_data',
            'kanban': await kanban_sv.get_whole_json(self.kanban_id),
        }))

    async def _update(self, payload):
        print('_update', payload)
        await kanban_sv.update_kanban(
            pipeline_id=payload['pipeLineId'],
            card_id_list=[x['id'] for x in payload['newCardList']]
        )
        # Send message to room group
        await self.channel_layer.group_send(
            self.kanban_name,
            {
                'type': 'updated',
                'payload': {}
            }
        )

    async def _add_card(self, payload):
        await kanban_sv.add_card(
            pipeline_id=payload['pipeLineId'],
            title=payload['title'],
            content=payload['content'],
            order=payload['order'],
        )
        # Send message to room group
        await self.channel_layer.group_send(
            self.kanban_name,
            {
                'type': 'updated',
                'payload': {}
            }
        )

    async def _add_pipeline(self, payload):
        await kanban_sv.add_pipeline(
            kanban_id=payload['kanbanId'],
            title=payload['title'],
            order=payload['order'],
        )
        # Send message to room group
        await self.channel_layer.group_send(
            self.kanban_name,
            {
                'type': 'updated',
                'payload': {}
            }
        )
