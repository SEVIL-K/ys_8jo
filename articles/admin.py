from django.contrib import admin
from articles.models import  Comment,Article

admin.site.register(Article)
admin.site.register(Comment)
