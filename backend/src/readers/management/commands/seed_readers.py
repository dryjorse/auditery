from django.core.management.base import BaseCommand
from readers.models import Reader
from faker import Faker

class Command(BaseCommand):
  help = 'Seed database with readers'

  def handle(self, *args, **kwargs):
    fake = Faker()

    for _ in range(3):
      Reader.objects.create(fullname=fake.name())
