# Generated by Django 5.0.6 on 2024-08-26 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_age_limit_alter_book_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название'),
        ),
    ]