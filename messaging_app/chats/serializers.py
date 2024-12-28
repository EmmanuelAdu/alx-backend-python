from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'password', 'email', 'phone_number', 'role', 'created_at', 'full_name']
    
    def get_full_name(self, obj):
        """Combine first name and last name to full name"""
        return f"{obj.first_name} {obj.last_name}"



class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    sender_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='sender', write_only=True
    )
    message_preview = serializers.CharField(source='message_body', read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'conversation', 'message_preview', 'message_body', 'sent_at']
    
    def validate_message_body(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Message body must be atleast 5 characters long")
        return value


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    participants_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, source='participants', write_only=True
    )
    messages = MessageSerializer(many=True, read_only=True)
    latest_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants_id', 'latest_message', 'messages', 'created_at']
    
    def get_latest_message(self, obj):
        """Retrieve the latest message in the conversation"""
        latest_message = obj.messages.order_by('-sent_at').first()
        if latest_message:
            return MessageSerializer(latest_message).data
        return None
