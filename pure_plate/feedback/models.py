from django.db import models
from restaurant.models import Restaurant

class Feedback(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='feedbacks')
    vegan = models.BooleanField(blank=True, null=True)
    halal = models.BooleanField(blank=True, null=True)
    gluten_free = models.BooleanField(blank=True, null=True)
    lacto_free = models.BooleanField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Feedback for {self.restaurant.name}"
