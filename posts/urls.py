from django.conf.urls import url, include
from . import views
from .api import PostsViewSet, UsersPostsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostsViewSet)

urlpatterns = router.urls

