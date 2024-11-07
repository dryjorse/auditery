from rest_framework.viewsets import ModelViewSet
from .models import Audio
from .serializers import AudioSerializer

class AudioView(ModelViewSet):
  queryset = Audio.objects.all()
  serializer_class = AudioSerializer