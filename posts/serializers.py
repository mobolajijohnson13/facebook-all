from rest_framework import serializers
from .models import Comments, Like, Post
from rest_framework.serializers import ModelSerializer

class PostSerializer(ModelSerializer):
    likes = serializers.IntegerField(source = "get_num_of_likes", read_only = True)
    comments = serializers.IntegerField(source = "get_num_of_comments", read_only = True)

    

    class Meta:
        model = Post
        fields = '__all__'
        # fields = ["text", "user","likes","created_on", "comments"]

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ["post","user"]





class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = ["post","user"]