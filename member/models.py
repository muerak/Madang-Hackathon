from django.db import models
from django.core.validators import RegexValidator, MinValueValidator


class Member(models.Model):
    phone_last_four = models.CharField(
        max_length=4,
        validators=[
            RegexValidator(r'^\d{4}$')
        ]
    )
    point = models.IntegerField(validators=[MinValueValidator(0)])
    barcode_image = models.ImageField(upload_to='barcode_images/%Y/%m/%d', blank=True)
    barcode_uploaded = models.DateField(auto_now=True)

    def __str__(self):
        return self.phone_last_four
