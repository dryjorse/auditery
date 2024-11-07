from rest_framework.viewsets import ModelViewSet
from .models import Book, Favorite
from .serializers import BookSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status, filters
from .serializers import FavoriteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from django.db.models import Avg, Value
from django.db.models.functions import Coalesce

class BookFilter(rest_framework.FilterSet):
  genres = rest_framework.BaseInFilter(field_name='genres', lookup_expr='in')
  selections = rest_framework.BaseInFilter(field_name='selections', lookup_expr='in')

  class Meta:
    model = Book
    fields = ['genres', 'selections']

class BooksView(ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
  search_fields = ['title', 'description']
  filterset_class = BookFilter
  ordering_fields = ['created_at']

  def get_queryset(self):
    queryset = super().get_queryset()
    ordering = self.request.query_params.get('ordering', None)

    if ordering == 'average_rating':
      queryset = queryset.annotate(average_rating=Coalesce(Avg('reviews__rating'), Value(0.0))).order_by("-average_rating")

    return queryset

class FavoriteToggleView(generics.GenericAPIView):
  serializer_class = FavoriteSerializer
  permission_classes = [permissions.IsAuthenticated]

  def post(self, request, *args, **kwargs):
    user = request.user
    book_id = request.data.get('book')

    try:
      book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
      return Response({"detail": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
    favorite, created = Favorite.objects.get_or_create(user=user, book=book)

    if not created:
      favorite.delete()
      return Response({"detail": "Removed from favorites."}, status=status.HTTP_204_NO_CONTENT)
    else:
      return Response({"detail": "Added to favorites."}, status=status.HTTP_201_CREATED)
