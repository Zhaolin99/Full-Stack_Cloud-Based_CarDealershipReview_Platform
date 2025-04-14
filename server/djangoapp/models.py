

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # founded_year = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('TRUCK', 'Truck'),
    ]
    type = models.CharField(max_length=100)
    year = models.IntegerField(default=2023, validators=[
                                                MaxValueValidator(2023),
                                                MinValueValidator(2015)])

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
