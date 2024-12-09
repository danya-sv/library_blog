from django.db import models

class BookModel(models.Model):
    GENRE = (
        ("Рассказ", "Рассказ"),
        ("Роман", "Роман"),
        ("Поэма", "Поэма"),
        ("Повесть", "Повесть"),
        ("Эпос", "Эпос")
    )
    image = models.ImageField(upload_to="books/", verbose_name="Загрузи фото книги")
    title = models.CharField(max_length=100, verbose_name="Укажи название книги")
    description = models.TextField(verbose_name="Укажите описание", blank=True)
    price = models.FloatField(verbose_name="Укажи цену книги", default=10)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, default="Не указано")
    mail = models.EmailField(max_length=254, verbose_name="Укажите почту автора", blank=True)
    name_author = models.CharField(max_length=20, default="Не указано")
    trailer = models.URLField(verbose_name="Укажи ссылку на трейлер")   


    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        
    def __str__(self):
        return self.title
