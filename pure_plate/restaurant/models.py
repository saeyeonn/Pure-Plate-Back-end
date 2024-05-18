from django.db import models

class Place(models.Model):
    PlaceID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Latitude = models.DecimalField(max_digits=10, decimal_places=8)
    Longitude = models.DecimalField(max_digits=11, decimal_places=8)
    reviewAmount = models.IntegerField(default=0)
    totalrating = models.IntegerField(default=0)
    AVGrating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=50)
    PlaceID = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='categories')

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)

class Favorite(models.Model):
    FavoriteID = models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Place = models.ForeignKey(Place, on_delete=models.CASCADE)

class Review(models.Model):
    ReviewID = models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Place = models.ForeignKey(Place, on_delete=models.CASCADE)
    Rating = models.IntegerField()
    ReviewText = models.TextField()
    VisitDate = models.DateField()
