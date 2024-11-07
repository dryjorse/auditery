from rest_framework.viewsets import ModelViewSet
from .models import Selection
from .serializers import SelectionSerializer

class SelectionsView(ModelViewSet):
  queryset = Selection.objects.all()
  serializer_class = SelectionSerializer