from django.db import models
from books.models import Book
from users.models import User

class Review(models.Model):
  RATING_CHOICES = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
  }

  rating = models.IntegerField(choices=RATING_CHOICES)
  comment = models.TextField("Отзыв")
  created_at = models.DateTimeField(auto_now_add=True)
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')


  class Meta:
    verbose_name = "Отзывы"
    verbose_name_plural = "Отзывы"
    unique_together = ('user', 'book')

  def __str__(self):
    return f'Отзыв о книге {self.book.title} от {self.user.username}'