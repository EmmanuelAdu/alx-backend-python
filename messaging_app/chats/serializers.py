from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'password', 'email', 'phone_number', 'role', 'created_at']


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    sender_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='sender', write_only=True
    )

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'conversation', 'message_body', 'sent_at']


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    participants_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, source='participants', write_only=True
    )
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants_id', 'created_at']