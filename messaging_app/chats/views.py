from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing conversations
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def create(self, request, *args, **kwargs):
        """
        """
        participants_ids = request.data.get("participants_id", [])
        if len(participants_ids) < 1:
            return Response(
                {"error": "A conversation must have at least two participants"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        participants = User.objects.filter(id__in=participants_ids)
        if participants.count() != len(participants_ids):
            return Response(
                {"error": "One or more participants do not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        conversation = Conversation.objects.create()
        conversation.participants.set(participants)
        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing messages.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        """
        Send a new message to an existing conversation.
        """
        conversation_id = request.data.get("conversation_id")
        sender_id = request.data.get("sender_id")
        message_body = request.data.get("message_body")

        # Validate inputs
        if not conversation_id or not sender_id or not message_body:
            return Response(
                {"error": "conversation_id, sender_id, and message_body are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            conversation = Conversation.objects.get(id=conversation_id)
        except Conversation.DoesNotExist:
            return Response(
                {"error": "Conversation does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            sender = User.objects.get(id=sender_id)
        except User.DoesNotExist:
            return Response(
                {"error": "Sender does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Create and save the message
        message = Message.objects.create(
            conversation=conversation, sender=sender, message_body=message_body
        )
        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)