from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=10)

    def __str__(self):
        return self.user.first_name