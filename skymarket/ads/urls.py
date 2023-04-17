from ads.views import AdViewSet, CommentViewSet
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

router = SimpleRouter()
router.register('ads', AdViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
