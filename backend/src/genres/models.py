from django.db import models

class Genre(models.Model):
  title = models.CharField("Название", max_length=250, unique=True)

  class Meta:
    verbose_name = "Жанры"
    verbose_name_plural = "Жанры"

  def __str__(self):
    return self.title
