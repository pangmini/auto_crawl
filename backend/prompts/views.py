from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation
from .serializers import ConversationSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        conversation = serializer.save()

        # 여기에 LLM 처리 로직을 추가할 수 있습니다
        # response = llm_model.generate(conversation.prompt)
        # conversation.response = response
        # conversation.save()

        return Response({
            'ok': True,
            'message': '입력이 처리되었습니다.',
            'data': serializer.data
        })