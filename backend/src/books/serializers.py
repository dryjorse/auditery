from rest_framework import serializers
from .models import Book, Favorite
from audio.serializers import AudioSerializer
from django.db.models import Avg

class BookSerializer(serializers.ModelSerializer):
  # audio = AudioSerializer(many=True, read_only=True)
  average_rating = serializers.SerializerMethodField()

  class Meta:
    model = Book
    fields = ["id", "title", "image", "age_limit", "authors", "reviews", "average_rating"] 
    read_only_fields = ['added_at']
    depth = 1

  def get_average_rating(self, obj):
    return obj.reviews.aggregate(average_rating=Avg('rating'))['average_rating'] or 0.0
  
class FavoriteSerializer(serializers.ModelSerializer):
  book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
  
  class Meta:
    model = Favorite
    fields = ['id', 'user', 'book', 'added_at']
    read_only_fields = ['user', 'added_at']