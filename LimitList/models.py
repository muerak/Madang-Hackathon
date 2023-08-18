from django.db import models

class LimitProduct(models.Model):

    limit_product_code = models.CharField(max_length=10)
    limit_product_name = models.CharField(max_length=100)
    limit_stock = models.PositiveIntegerField()
    limit_regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    limit_discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    limit_product_image = models.ImageField(upload_to='limit_product_images/%Y/%m/%d', blank=True)
    limit_uploaded = models.DateField(auto_now=True)

    def __str__(self):
        return self.limit_product_name
