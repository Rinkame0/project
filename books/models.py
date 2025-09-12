from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField("Назва", max_length=255)
    author = models.CharField("Автор", max_length=255)
    genre = models.CharField("Жанр", max_length=100)
    cover_image = models.URLField("Фото", blank=True, null=True)
    year = models.PositiveIntegerField("Рік", blank=True, null=True)
    description = models.TextField("Опис", blank=True)
    country = models.CharField("Країна", max_length=100, blank=True)

    def __str__(self):
        return f"{self.title} — {self.author}"