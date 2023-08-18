from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('FF', '신선식품'),
        ('PF', '가공식품'),
        ('DN', '생활용품'),
    )

    product_code = models.CharField(max_length=10)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images/%Y/%m/%d', blank=True)
    product_uploaded = models.DateField(auto_now=True)

    def __str__(self):
        return self.product_name
