# Generated by Django 5.0.6 on 2024-08-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='fullname',
            field=models.CharField(max_length=50, verbose_name='Полное имя'),
        ),
    ]
