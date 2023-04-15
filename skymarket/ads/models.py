from django.conf import settings
from django.db import models
from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='ad_img/', null=True, blank=True)
    price = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=1000)


class Comment(models.Model):
    text = models.CharField(max_length=500, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, null=False)
