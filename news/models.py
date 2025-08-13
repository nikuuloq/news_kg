from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()  # Основной текст новости
    image = models.ImageField(upload_to='news_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
