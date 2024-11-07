from rest_framework.viewsets import ModelViewSet
from .models import Genre
from .serializers import GenreSerializer

class GenresView(ModelViewSet):
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer
