# Generated by Django 5.1.3 on 2024-12-09 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='books/', verbose_name='Загрузи фото книги')),
                ('title', models.CharField(max_length=100, verbose_name='Укажи название книги')),
                ('description', models.TextField(blank=True, verbose_name='Укажите описание')),
                ('price', models.FloatField(default=10, verbose_name='Укажи цену книги')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('genre', models.CharField(choices=[('Рассказ', 'Рассказ'), ('Роман', 'Роман'), ('Поэма', 'Поэма'), ('Повесть', 'Повесть'), ('Эпос', 'Эпос')], default='Не указано', max_length=100)),
                ('mail', models.EmailField(blank=True, max_length=254, verbose_name='Укажите почту автора')),
                ('name_author', models.CharField(default='Не указано', max_length=20)),
                ('trailer', models.URLField(verbose_name='Укажи ссылку на трейлер')),
            ],
        ),
    ]