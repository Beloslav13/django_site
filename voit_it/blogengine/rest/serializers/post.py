from rest_framework import serializers
from blogengine.models.posts import Post


class PostSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
