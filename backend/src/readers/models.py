from django.db import models

class Reader(models.Model):
  fullname = models.CharField("Полное имя", max_length=50)
  
  class Meta:
    verbose_name = "Читатели"
    verbose_name_plural = "Читатели"

  def __str__(self):
    return self.fullname