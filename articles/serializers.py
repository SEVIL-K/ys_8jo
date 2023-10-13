from rest_framework import serializers
from articles.models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Comment
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comment_set = CommentSerializer(many=True)
    likes = serializers.StringRelatedField(many=True)

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Article
        fields = '__all__'

# class PictureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ArticlePicture
#         fields = ('picture',)
class ArticleCreateSerializer(serializers.ModelSerializer):
    # pictures = PictureSerializer(many=True, source='pictures', read_only=True)
    class Meta:
        model = Article
        fields = ("title", "content", "picture",)



class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_comments_count(self, obj):
        return obj.comment_set.count()

    class Meta:
        model = Article
        fields = ("pk", "title", "picture", "updated_at", "user", "likes_count", "comments_count")


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content",)