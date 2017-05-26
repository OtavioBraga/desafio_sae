from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Purchase, Product


@receiver(post_save, sender=Purchase)
def update_product_quantity(sender, instance, **kwargs):
    instance.product.quantity += instance.quantity
    instance.product.save()