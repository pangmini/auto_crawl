from rest_framework import serializers
from .models import Conversation

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['id', 'prompt', 'timestamp', 'response', 'metadata']
        read_only_fields = ['id', 'timestamp']