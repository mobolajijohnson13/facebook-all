from posts.models import Like
from posts.views import CommentsViewSet, LikeViewSet, tone
from django.urls import path,include
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from posts.views import PostViewSet, tone


router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'like', LikeViewSet)
router.register(r'comments', CommentsViewSet)

urlpatterns = [
    
    path("tone/", tone),
    path("", include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]



 