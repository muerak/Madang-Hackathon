from django.core.validators import MaxValueValidator
from django.db import models
from LimitList.models import LimitProduct

class Reservation(models.Model):
    reservation_product = models.ForeignKey(LimitProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

    def __str__(self):
        return f"{self.reservation_product} - {self.quantity}개 예약"
