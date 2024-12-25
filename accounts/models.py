from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models
from django.utils import timezone
from django.conf import settings
import uuid
from django.utils import timezone
from datetime import timedelta

class CustomManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)  
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)  

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)




class CustomUser(AbstractUser):
    username = None  
    email = models.EmailField(unique=True)  
    first_name = models.CharField(max_length=100, blank=True)  
    last_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomManager()

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []  

    def __str__(self):
        return self.email

class EmailVerification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(hours=24)
        super().save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() > self.expires_at
    
    def __str__(self):
        return f"Token for {self.user.email} - {self.token}"
