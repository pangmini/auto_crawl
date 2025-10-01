from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from prompts.views import ConversationViewSet

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]