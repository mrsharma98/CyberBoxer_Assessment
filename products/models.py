from django.db import models

from accounts.models import UserProfileInfo
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    hunter = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
