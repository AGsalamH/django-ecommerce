from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('A user must have an email address.')
        if not password:
            raise ValueError('Password must be set.')
        
        user = self.model(
            email = self.normalize_email(email),
            password = make_password(password),
            **extra_fields
        )
        user.save()
        return user
    
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        if extra_fields.get('is_staff') is True:
            raise ValueError('A user must have is_staff=False.')
        if extra_fields.get('is_superuser') is True:
            raise ValueError('A user must have is_superuser=False.')

        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('A superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('A user must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
        