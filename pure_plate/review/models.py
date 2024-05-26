from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from account.models import User
from restaurant.models import Restaurant

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField()
    visit_date = models.DateField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.restaurant.update_rating()
