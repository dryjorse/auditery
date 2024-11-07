from django.db import models
from django.core.exceptions import ValidationError
from authors.models import Author
from readers.models import Reader
from genres.models import Genre
from selections.models import Selection
from users.models import User
import os

def validate_age_limit(value):
  if value > 30:
    raise ValidationError(_("%(value)s не должен быть больше 30"), params={"value": value},)

def validate_image_file_extension(value):
  ext = os.path.splitext(value.name)[1]
  valid_extensions = ['.jpg', '.jpeg', '.png']
  if not ext.lower() in valid_extensions:
    raise ValidationError(f'Непподерживаемое расширения файла. Поддерживаемые расширения: {", ".join(valid_extensions)}')

class Book(models.Model):
  title = models.CharField("Название", max_length=100, unique=True)
  image = models.ImageField("Картинка", upload_to="images/books", validators=[validate_image_file_extension])
  age_limit = models.PositiveSmallIntegerField("Возрастное ограничение", blank=True, null=True, validators=[validate_age_limit])
  description = models.TextField("Описание")
  price = models.DecimalField("Цена", max_digits=5, decimal_places=2)
  wk = models.CharField("В контакте", max_length=250, blank=True)
  instagram = models.CharField("Инстаграмм", max_length=250, blank=True)
  facebook = models.CharField("Фейсбук", max_length=250, blank=True)
  youtube = models.CharField("Ютуб", max_length=250, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
  authors = models.ManyToManyField(Author)
  genres = models.ManyToManyField(Genre)
  selections = models.ManyToManyField(Selection, blank=True)

  class Meta:
    verbose_name = "Книги"
    verbose_name_plural = "Книги"

  def __str__(self):
    return self.title
    
class Favorite(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='favorited_by')
  added_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    unique_together = ('user', 'book')