from django.db import models

class Place(models.Model):
    PlaceID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, db_index=True)
    Address = models.CharField(max_length=255)
    Latitude = models.DecimalField(max_digits=10, decimal_places=8)
    Longitude = models.DecimalField(max_digits=11, decimal_places=8)
    reviewAmount = models.IntegerField(default=0)
    totalrating = models.IntegerField(default=0)
    AVGrating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
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
