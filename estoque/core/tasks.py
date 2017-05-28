from .models import Purchase, Product
from django.db.models import Sum
from celery import shared_task
from time import sleep


@shared_task(bind=True)
def calculate_average_price(self, product_id):
    '''
    Take all purchases of a product and calculate the average coast.
    The average coast may change if a new purchase is made.
    The calc is made based on the coast of all purchases from a product
    divided by the all units purchsed.
    '''
    sleep(60)
    values = Purchase.objects.filter(
        product_id=product_id
    ).aggregate(Sum('value'), Sum('quantity'))

    average_coast = values['value__sum'] / values['quantity__sum']
    average_coast = round(average_coast, 2)

    product = Product.objects.get(id=product_id)
    product.average_coast = average_coast
    product.save()
