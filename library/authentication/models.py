from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Електронна пошта обов'язкова для заповнення")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('role', 1)  # 1 - Бібліотекар/Адмін за замовчуванням
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    role = models.IntegerField(default=0)  # 0 - Звичайний користувач (Гість), 1 - Бібліотекар
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    @property
    def is_superuser(self):
        return self.role == 1

    @property
    def is_staff(self):
        return self.role == 1


    def has_perm(self, perm, obj=None):
        return self.role == 1

    def has_module_perms(self, app_label):
        return self.role == 1

    def __str__(self):
        return self.email