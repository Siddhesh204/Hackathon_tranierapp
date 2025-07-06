# Django models for a training timetable application
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission

class MemberManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Member(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=128)

    objects = MemberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Override groups with a unique related_name
    groups = models.ManyToManyField(
        Group,
        related_name='member_groups',  # Unique reverse accessor
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.',
    )

    # Override user_permissions with a unique related_name
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='member_permissions',  # Unique reverse accessor
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.email

class Trainer(models.Model):
    user = models.OneToOneField(Member, on_delete=models.CASCADE, related_name='trainer')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Utilization(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    session_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.course_name} on {self.session_date}"