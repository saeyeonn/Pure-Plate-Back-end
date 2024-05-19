from django.db import models
from django.db.models import Avg
from account.models import User 

class Restaurant(models.Model):
    RestaurantID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, db_index=True)
    Address = models.CharField(max_length=255)
    Latitude = models.DecimalField(max_digits=10, decimal_places=8)
    Longitude = models.DecimalField(max_digits=11, decimal_places=8)
    reviewCount = models.IntegerField(default=0)
    avgRating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    categories = models.ManyToManyField('Category', related_name='places')

    class Meta:
        indexes = [
            models.Index(fields=['Name']),
        ]

class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)

    CategoryName = models.CharField(max_length=50, db_index=True)

   


    class Meta:
        indexes = [
            models.Index(fields=['CategoryName']),
        ]

class Review(models.Model):
    ReviewID = models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Rating = models.IntegerField()
    ReviewText = models.TextField()
    VisitDate = models.DateField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        restaurant = self.Restaurant

        restaurant.reviewCount = Review.objects.filter(Restaurant=restaurant).count()
        restaurant.avgRating = Review.objects.filter(Restaurant=restaurant).aggregate(total_rating=Avg('Rating'))['total_rating']

        restaurant.save()
