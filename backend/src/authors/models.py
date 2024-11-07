from django.db import models

class Author(models.Model):
  fullname = models.CharField("Имя", max_length=50)
  description = models.TextField("Описание")

  class Meta:
    verbose_name = "Автора"
    verbose_name_plural = "Автора"

  def __str__(self):
    return self.fullname
