from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employee(models.Model):
    user = models.ForeignKey(
        User, related_name="user_employee", on_delete=models.CASCADE, default=1
    )
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.first_name
