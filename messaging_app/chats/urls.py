from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import ConversationViewSet, MessageViewSet


# Create the root router
router = NestedDefaultRouter()

# Register the conversation viewset
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Nested router for messages within conversation
conversations_router = NestedDefaultRouter(router, r'conversations', loopup='conversation')
conversations_router.register(r'messages', MessageViewSet, basename='conversation-messages')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)), # include main router
    path('', include(conversations_router.urls)), # include nested router
]