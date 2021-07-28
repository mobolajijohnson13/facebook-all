from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,HttpResponse
from django.shortcuts import render
from posts.serializers import CommentsSerializer, LikeSerializer,PostSerializer
from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import Comments, Like, Post

# Create your views here.


def tone(request):
    return HttpResponse("Hello Liberty")


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    # permission_classes = [permissions.IsAuthenticated]



class CommentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    # permission_classes = [permissions.IsAuthenticated]