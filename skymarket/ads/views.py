from ads.models import Ad, Comment
from ads.serializers import CommentSerializer
from rest_framework import pagination, viewsets


class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    pass


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = AdPagination
    # def perform_create(self, serializer):
    #     # serializer.save(author = self.request.user, ad = self.kwargs.get('pk...')
    #     return super().perform_create(serializer)
