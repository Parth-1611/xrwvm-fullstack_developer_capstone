from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    # Many-to-one relationship: one car make can have many car models
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    # Dealer ID refers to a dealer created in the Cloudant database
    dealer_id = models.IntegerField(default=0)
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Wagon', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[MaxValueValidator(2026), MinValueValidator(2015)]
    )

    def __str__(self):
        return self.car_make.name + " " + self.name
