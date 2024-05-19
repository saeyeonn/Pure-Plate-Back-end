from django.db import models

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from account.models import User
from restaurant.models import Restaurant

class Review(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    ReviewText = models.TextField()
    VisitDate = models.DateField()