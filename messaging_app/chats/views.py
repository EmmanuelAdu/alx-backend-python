from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, and retrieving conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    @action(detail=False, methods=['post'])
    def create_conversation(self, request):
        """
        Custom endpoint for creating a new conversation.
        Expects a list of participant IDs in the request data.
        """
        participant_ids = request.data.get('participants', [])
        participants = User.objects.filter(id__in=participant_ids)
        if len(participant_ids) != participants.count():
            return Response({'error': 'One or more participants not found.'}, status=400)
        
        conversation = Conversation.objects.create()
        conversation.participants.set(participants)
        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=201)


class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, and retrieving messages.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['sent_at']
    ordering = ['-sent_at']

    @action(detail=False, methods=['post'])
    def send_message(self, request, pk=None):
        """
        Custom endpoint for sending a message to an existing conversation.
        Expects the conversation ID and message body in the request data.
        """
        conversation_id = request.data.get('conversation_id')
        message_body = request.data.get('message_body')
        sender = request.user

        conversation = get_object_or_404(Conversation, id=conversation_id)
        message = Message.objects.create(
            sender=sender,
            conversation=conversation,
            message_body=message_body
        )
        serializer = self.get_serializer(message)
        return Response(serializer.data, status=201)
