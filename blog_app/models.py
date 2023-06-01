from django.db import models

# Create your models here
class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=128)
    description = models.CharField(max_length=512, null=True)

    def __str__(self):
        return self.title

class Comment (models.Model):
    author = models.CharField(max_length=128)
    message = models.CharField(max_length=255)
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE)

    def __str__(self):
        return self.title