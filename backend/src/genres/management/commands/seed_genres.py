from django.core.management.base import BaseCommand
from genres.models import Genre
from faker import Faker

class Command(BaseCommand):
  help = 'Seed database with genres'

  def handle(self, *args, **kwargs):
    fake = Faker()

    for _ in range(10):
      Genre.objects.create(title=fake.word())