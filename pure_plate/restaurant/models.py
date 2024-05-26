from django.db import models
from django.db.models import Avg

# class Category(models.Model):
#     category_id = models.AutoField(primary_key=True)
#     category_name = models.CharField(max_length=50, db_index=True)

#     class Meta:
#         verbose_name_plural = "categories"

class Restaurant(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    time = models.CharField(max_length=255, db_index=True)
    photo = models.CharField(max_length=255, db_index=True)
    phone = models.CharField(max_length=255, db_index=True)
    review_count = models.IntegerField(default=0)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    # categories = models.ManyToManyField(Category, related_name='restaurants')
    vegan=models.BooleanField(default=False)
    halal=models.BooleanField(default=False)
    gluten_free=models.BooleanField(default=False)
    lacto_free=models.BooleanField(default=False)

    def update_rating(self):
        self.review_count = self.review_set.count()
        if self.review_count > 0:
            self.avg_rating = self.review_set.aggregate(avg_rating=Avg('rating'))['avg_rating']
        else:
            self.avg_rating = 0.00
        self.save()
