from django.db import models
from django.contrib.auth.models import User

# -----------------------------------------
# FixModel
# -----------------------------------------
class FixModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



# -----------------------------------------
# Car
# -----------------------------------------
from django.core.validators import MinValueValidator

class Car(FixModel):

    GEAR = (
        (1, 'Auto'),
        (0, 'Manual'),
    )

    plate = models.CharField(max_length=16, unique=True)
    brand = models.CharField(max_length=16)
    model = models.CharField(max_length=16)
    year = models.PositiveSmallIntegerField()
    gear = models.BooleanField(choices=GEAR, default=0)
    rent_per_day = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(1)],
    )
    availabilty = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.brand} {self.model} {self.plate}'


# -----------------------------------------
# Reservarion
# -----------------------------------------
class Reservation(FixModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    started_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Customer {self.user} reserved {self.car} - {self.start_date} - {self.end_date}"