from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    rating = models.FloatField()
    image = models.URLField()

    def __str__(self):
        return self.name

class Review(models.Model):
    author = models.ForeignKey(User)
    review_text = models.TextField()
    rating = models.FloatField()
    restaurant = models.ForeignKey('Restaurant',null=True)
    
    def __str__(self):
        return u"{}-{}".format(self.author.username, self.restaurant.name)
