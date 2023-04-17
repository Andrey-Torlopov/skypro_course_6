from rest_framework.permissions import BasePermission
from users.models import UserRole


class IsAdOwner(BasePermission):
    message = "У вас нет прав на изменение объявления"

    def has_object_permission(self, request, view, ad) -> bool:
        if request.user == ad.author or request.user.role == UserRole.ADMIN:
            return True
        return False
