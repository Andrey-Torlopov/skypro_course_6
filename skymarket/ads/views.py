from ads.models import Ad, Comment
from ads.serializers import AdDetailSerializer, AdSerializer, CommentSerializer
from rest_framework import pagination, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated


class AdPagination(pagination.PageNumberPagination):
    page_size = 10


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    default_serializer = AdSerializer
    pagination_class = AdPagination

    serializer_classes = {
        "retrieve": AdDetailSerializer,
        "list": AdSerializer
    }

    default_permission = [AllowAny()]
    permissions_list = {
        "retrieve": [IsAuthenticated()]
    }

    def get_serializer_class(self) -> AdSerializer | AdDetailSerializer:
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_permissions(self) -> IsAuthenticated | AllowAny:
        return self.permissions_list.get(self.action, self.default_permission)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = AdPagination
    # def perform_create(self, serializer):
    #     # serializer.save(author = self.request.user, ad = self.kwargs.get('pk...')
    #     return super().perform_create(serializer)
