from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return 'Profile of user {}'.format(self.user.username)





# class Auto(models.Model):
#     marka = models.TextField(User, on_delete=models.CASCADE)
#     nomer = models.DateField(null=True, blank=True)