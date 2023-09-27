from rest_framework import serializers

# class ArticleListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(allow_blank=True, max_length=100)
#     body = serializers.CharField(allow_blank=True)
#     created = serializers.DateTimeField()
#     updated = serializers.DateTimeField()



from rest_framework import serializers
from article.models import Article
from user_info.serializers import UserDescSerializer


# 父类变成了 ModelSerializer
# class ArticleListSerializer(serializers.ModelSerializer):
#     author = UserDescSerializer(read_only=True)
#     # 新增字段，添加超链接
#     url = serializers.HyperlinkedIdentityField(view_name="article:detail")
#     class Meta:
#         model = Article
#         fields = [
#             'id',
#             'url',
#             'title',
#              'created',
#             'author',
#         ]
#
#
#
# class ArticleDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'