# Generated by Django 5.0.6 on 2024-08-26 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.CharField(max_length=250, unique=True, verbose_name='Название'),
        ),
    ]
