from django.core.management.base import BaseCommand
from authors.models import Author
from faker import Faker

class Command(BaseCommand):
  help = 'Seed database with authors'

  def handle(self, *args, **kwargs):
    fake = Faker()

    for _ in range(3):
      Author.objects.create(fullname=fake.name(), description=fake.sentences(nb=8))
