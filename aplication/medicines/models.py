from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Medications(models.Model):
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
        
    def __str__(self):
        return f'{self.description} - User:  {self.user.username}'