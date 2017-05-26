from datetime import datetime
from django.db import models


class Product(models.Model):
    name = models.CharField(
        'Nome do produto',
        max_length=100,
        blank=False,
        null=False
    )

    average_coast = models.DecimalField(
        'Preço médio',
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True
    )

    quantity = models.IntegerField('Quantidade', default=0)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Purchase(models.Model):
    product = models.ForeignKey(Product)

    value = models.DecimalField(
        "Valor da total da compra", 
        max_digits=8,
        decimal_places=2,
    )

    quantity = models.IntegerField('Quantidade', default=1)

    purchase_date = models.DateTimeField(
        'Data da compra',
        default=datetime.now()
    )

    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

    def unit_price(self):
        unit_price = self.value / self.quantity
        return round(unit_price, 2)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
