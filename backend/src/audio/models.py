from django.db import models
from books.models import Book
from mutagen.mp3 import MP3

class Audio(models.Model):
  title = models.CharField("Название", max_length=250)
  part = models.IntegerField("Часть")
  audio = models.FileField(upload_to="audios/")
  book = models.ForeignKey(Book, related_name='audio', on_delete=models.CASCADE)
  duration = models.FloatField(editable=False, null=True, blank=True)

  class Meta:
    verbose_name = "Аудио"
    verbose_name_plural = "Аудио"

  def __str__(self):
    return self.title
  
  def save(self, *args, **kwargs):
    if not self.duration and self.audio:
      audio = MP3(self.audio)
      self.duration = audio.info.length
    super().save(*args, **kwargs)