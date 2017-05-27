from django.db.models.signals import post_save, pre_delete
from .tasks import calculate_average_price
from django.dispatch import receiver
from .models import Purchase, Task


@receiver(post_save, sender=Purchase)
def increase_product_quantity(sender, instance, **kwargs):
    instance.product.quantity += instance.quantity
    instance.product.save()
    task = calculate_average_price.delay(instance.product.id).id
    Task.objects.create(task_id=task)


@receiver(pre_delete, sender=Purchase)
def decrease_product_quantity(sender, instance, **kwargs):
    instance.product.quantity -= instance.quantity
    instance.product.save()
    calculate_average_price.delay(instance.product.id)