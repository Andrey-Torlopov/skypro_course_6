import json

from ads.models import Ad, Comment
from django.http import JsonResponse
# from attr import field
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdUpdateSerializer(serializers.ModelSerializer):
    author = serializers.IntegerField(read_only=True)
    created_at = serializers.DateField(read_only=True)

    class Meta:
        model = Ad
        fields = ["id", "title", "price",
                  "author", "created_at", "description"]

    def patch(self, request, *args, **kwargs) -> JsonResponse:
        super().post(request, *args, **kwargs)

        data = json.loads(request.body)

        self.object.title = data["title"]
        self.object.price = int(data["price"])
        self.object.description = data["description"]

        self.object.save()

        return JsonResponse({
            "id": self.object.pk,
            "title": self.object.name,
            "price": self.object.price,
            "description": self.object.description
        })


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["id"]
