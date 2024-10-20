from django.db import models


class Page(models.Model):
    url = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.IntegerField(default=0)  # Количество заголовков h1
    subtitle = models.IntegerField(default=0)  # Количество заголовков h2
    content = models.IntegerField(default=0)  # Количество заголовков h3
    links = models.JSONField(default=list)  # Список найденных ссылок

    def __str__(self):
        return self.url
