from rest_framework import viewsets

from .models import Resume
from .permissions import IsOwnerOrReadOnly
from .serializers import ResumeSerializer


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsOwnerOrReadOnly]
