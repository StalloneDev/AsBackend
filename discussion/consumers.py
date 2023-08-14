import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Discussion, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.discussion_id = self.scope['url_route']['kwargs']['discussion_id']
        self.discussion_group_name = f"discussion_{self.discussion_id}"

        # Ajouter l'utilisateur à la discussion group
        await self.channel_layer.group_add(
            self.discussion_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Supprimer l'utilisateur de la discussion group
        await self.channel_layer.group_discard(
            self.discussion_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        # Sauvegarder le message dans la base de données
        auteur = self.scope['user']
        discussion = Discussion.objects.get(id=self.discussion_id)
        Message.objects.create(discussion=discussion, auteur=auteur, contenu=message)

        # Envoyer le message à tous les utilisateurs dans la discussion group
        await self.channel_layer.group_send(
            self.discussion_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'auteur': auteur.username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        auteur = event['auteur']

        # Envoyer le message au WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'auteur': auteur
        }))