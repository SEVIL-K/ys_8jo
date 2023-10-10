from django.db import models
from accounts.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article")

    likes = models.ManyToManyField(User, related_name="likes", blank=True)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    review = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comment_set")


class ArticlePicture(models.Model):
    picture = models.DateField(blank=True)
    review = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="review")

