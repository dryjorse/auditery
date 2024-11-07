from django.core.management.base import BaseCommand
from selections.models import Selection
from django.core.files import File
from django.conf import settings
from faker import Faker
import random, os

class Command(BaseCommand):
  help = 'Seed database with selections'

  def handle(self, *args, **kwargs):
    fake = Faker()
    image_dir = os.path.join(settings.MEDIA_ROOT, 'term')
    image_files = os.listdir(image_dir)

    def get_image_file():
      return os.path.join(image_dir, random.choice(image_files))

    selection_one = Selection.objects.create(title="В дороге")
    with open(get_image_file(), 'rb') as img:
      selection_one.image.save(os.path.basename(get_image_file()), File(img), save=True)
    selection_two = Selection.objects.create(title="Для отдыха")
    with open(get_image_file(), 'rb') as img:
      selection_two.image.save(os.path.basename(get_image_file()), File(img), save=True)
    selection_three = Selection.objects.create(title="Для учебы")
    with open(get_image_file(), 'rb') as img:
      selection_three.image.save(os.path.basename(get_image_file()), File(img), save=True)
    selection_four = Selection.objects.create(title="Для работы")
    with open(get_image_file(), 'rb') as img:
      selection_four.image.save(os.path.basename(get_image_file()), File(img), save=True)