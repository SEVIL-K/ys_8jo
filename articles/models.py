from django.db import models
from accounts.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article")
    likes = models.ManyToManyField(User, related_name="like_articles", blank=True)
    picture = models.ImageField(null=True, blank=True)
    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    review = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comment_set")
    



