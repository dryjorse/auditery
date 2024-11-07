from django.core.management.base import BaseCommand
from books.models import Book 
from readers.models import Reader 
from authors.models import Author
from selections.models import Selection
from genres.models import Genre
from django.core.files import File
from django.conf import settings
from faker import Faker
import random, os

class Command(BaseCommand):
    help = 'Seed database with books'

    def handle(self, *args, **kwargs):
      fake = Faker()

      image_dir = os.path.join(settings.MEDIA_ROOT, 'term')

      image_files = os.listdir(image_dir)

      def get_image_file():
        return os.path.join(image_dir, random.choice(image_files))

      readers = random.sample(list(Reader.objects.all()), 3)
      authors = random.sample(list(Author.objects.all()), 3)
      genres = random.sample(list(Genre.objects.all()), 3)
      selections = list(Selection.objects.all())

      for _ in range(10):
        book = Book.objects.create(
          title=' '.join(fake.words(nb=2)),
          age_limit=random.choice([18, 0]),
          description=fake.sentences(nb=5),
          price=fake.random_int(0, 500),
          reader=random.choice(readers)
        )
        with open(get_image_file(), 'rb') as img:
          book.image.save(os.path.basename(get_image_file()), File(img), save=True)
        
        selected_authors = random.sample(authors, random.choice([1, 2]))
        book.authors.add(*selected_authors)
        book.selections.add(*[random.choice([selections[0], selections[1], selections[2], selections[3]])])
        book.genres.add(*random.sample(genres, 3))

      self.stdout.write(self.style.SUCCESS('Database seeded successfully'))