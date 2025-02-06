from rest_framework import permissions


class IsParticipantOfConversation(permissions.BasePermission):
    """Allow only authenticated users to access conversation and also allow
    only participants in a conversation to view and access that conversation
    """
    def has_object_permission(self, request, view):
        """ Ensure user is authenticated """
        return bool(request.user and request.user.is_authenticated)
    
    def has_conversation_permission(self, request, obj, view):
        """Allow participants in a conversation to access the conversation
        """
        if hasattr(obj, 'participants_id'):
            return request.user in obj.participants_id.all()
        
        # for messages check if user is participants

### We need to ensure that the person who is editing the message is the user or the person who has the write permission is the user

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow only senders of a message to edit it
    """

    def has_permission(self, request, view):
        # check if user is authenticated
        return bool(request.user and request.user.is_authenticated)
    
    def has_obj_permission(self, request, obj, view):
        # sender has write permissions
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # write permissions will only be allowed to owner of message
        return obj.sender_id == request.user