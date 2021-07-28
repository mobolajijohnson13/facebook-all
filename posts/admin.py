from django.contrib import admin

# Register your models here.
from posts.apps import PostsConfig
import posts
from django.contrib import admin
from posts.models import Comments, Like, Post
from django.contrib import admin
# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comments)
