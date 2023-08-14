from django.urls import path
from .views import DiscussionListCreateAPIView, DiscussionRetrieveUpdateDestroyAPIView, MessageListCreateAPIView, MessageRetrieveUpdateDestroyAPIView


urlpatterns = [
    
    path('api/discussions/', DiscussionListCreateAPIView.as_view(), name='discussion-list-create'),
    path('api/discussions/<int:pk>/', DiscussionRetrieveUpdateDestroyAPIView.as_view(), name='discussion-detail'),
    path('api/messages/', MessageListCreateAPIView.as_view(), name='message-list-create'),
    path('api/messages/<int:pk>/', MessageRetrieveUpdateDestroyAPIView.as_view(), name='message-detail'),
    
]