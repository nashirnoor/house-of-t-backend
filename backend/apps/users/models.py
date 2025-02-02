from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class User(AbstractUser):
    ROLES = (
        ('branch_manager', 'Branch Manager'),
        ('admin', 'Admin'),
    )
    phone_number = models.CharField(max_length=15, blank=True)
    role = models.CharField(max_length=20, choices=ROLES)

    def save(self, *args, **kwargs):
        if self.role == 'admin':
            self.is_staff = True
            self.is_superuser = True
        elif self.role == 'branch_manager':
            self.is_staff = False
            self.is_superuser = False

        super().save(*args, **kwargs)

        if self.role == 'admin':
            admin_group, _ = Group.objects.get_or_create(name='Admin')
            self.groups.add(admin_group)
        elif self.role == 'branch_manager':
            branch_manager_group, _ = Group.objects.get_or_create(name='Branch Manager')
            self.groups.add(branch_manager_group)


class Notification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications",
        null=True,
        blank=True,
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.message[:50]}..."

