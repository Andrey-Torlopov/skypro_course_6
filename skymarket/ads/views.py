from ads.models import Ad, Comment
from ads.permissions import IsAdOwner
from ads.serializers import (AdCreateSerializer, AdDetailSerializer,
                             AdSerializer, CommentCreateSerializer,
                             CommentSerializer)
from rest_framework import pagination, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated


class AdPagination(pagination.PageNumberPagination):
    page_size = 10


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    default_serializer = AdSerializer
    serializer_classes = {
        "create": AdCreateSerializer
    }

    default_permission = [AllowAny()]
    permissions_list = {
        "retrieve": [IsAuthenticated()],
        "create": [IsAuthenticated()],
        "update": [IsAuthenticated(), IsAdOwner()],
        "partial_update": [IsAuthenticated(), IsAdOwner()],
    }

    def get_serializer_class(self) -> AdSerializer | AdDetailSerializer:
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_permissions(self) -> IsAuthenticated | AllowAny:
        return self.permissions_list.get(self.action, self.default_permission)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    pagination_class = AdPagination

    default_serializer = CommentSerializer
    serializer_classes = {
        "create": CommentCreateSerializer
    }

    default_permission = [AllowAny()]
    permissions_list = {
        "retrieve": [IsAuthenticated()],
        "create": [IsAuthenticated()],
        "update": [IsAuthenticated(), IsAdOwner()],
        "partial_update": [IsAuthenticated(), IsAdOwner()],
    }

    def get_serializer_class(self) -> AdSerializer | AdDetailSerializer:
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_permissions(self) -> IsAuthenticated | AllowAny:
        return self.permissions_list.get(self.action, self.default_permission)
