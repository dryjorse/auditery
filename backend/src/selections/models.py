from django.db import models

class Selection(models.Model):
  title = models.CharField("Название", max_length=250, unique=True)
  image = models.ImageField("Картинка", upload_to="images/selections")

  class Meta:
    verbose_name = "Подборки"
    verbose_name_plural = "Подборки"

  def __str__(self):
    return self.title