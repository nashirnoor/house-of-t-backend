from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.branches.models import ProductRequest
from apps.reports.models import ProductOutflow
from apps.users.models import User, Notification


@receiver(post_save, sender=ProductRequest)
def create_product_request_notification(sender, instance, created, **kwargs):
    if created:
        # Notify all admin users
        admin_users = User.objects.filter(role='admin')
        for admin in admin_users:
            Notification.objects.create(
                user=admin,
                message=f"New product request: {instance.quantity} x {instance.product.name} requested by {instance.branch.name}"
            )


@receiver(post_save, sender=ProductOutflow)
def create_product_outflow_notification(sender, instance, created, **kwargs):
    if created:
        # Notify the branch manager
        branch_manager = instance.branch.manager
        if branch_manager:
            Notification.objects.create(
                user=branch_manager,
                message=f"Product outflow: {instance.quantity_sent} x {instance.product.name} sent to your branch"
            )
