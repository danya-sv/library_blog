# Generated by Django 5.1.3 on 2024-12-12 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_blog', '0002_alter_bookmodel_options_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]