from .models import Posts, UsersPosts
from rest_framework import serializers

class PostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = ('post_id', 'caption', 'image_path', 'date_created')

class UsersPostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsersPosts
        fields = ('post_id_id', 'user_id_id', 'is_liked', 'is_owner')