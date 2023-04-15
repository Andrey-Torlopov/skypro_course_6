from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from users.managers import UserManager, UserRole
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    phone = PhoneNumberField()
    email = models.CharField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=500)
    role = models.CharField(
        max_length=8, choices=UserRole.choices, default=UserRole.USER)
    image = models.ImageField(
        upload_to='user_avatars/', blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    @property
    def is_superuser(self) -> bool:
        return self.is_admin

    @property
    def is_staff(self) -> bool:
        return self.is_admin

    @property
    def is_admin(self) -> bool:
        return self.role == UserRole.ADMIN

    @property
    def is_user(self) -> bool:
        return self.role == UserRole.USER

    def has_perm(self, perm, obj=None) -> bool:
        return self.is_admin

    def has_module_perms(self, app_label) -> bool:
        return self.is_admin

    # также для работы модели пользователя должен быть переопределен
    # менеджер объектов
    objects = UserManager()
