from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import PostsSerializer, UsersPostsSerializer
from .models import Posts, UsersPosts


class PostsViewSet(ModelViewSet):
	queryset = Posts.objects.all()
	serializer_class = PostsSerializer
	permission_classes = (permissions.IsAuthenticated,)

class UsersPostsViewSet(ModelViewSet):
	queryset = UsersPosts.objects.all()
	serializer_class = UsersPostsSerializer
	permission_classes = (permissions.IsAuthenticated,)