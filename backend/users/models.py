from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Extend Django's Buitl-In User Model Uinsg a One-to-One databse rmodle relationship
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_photo = models.ImageField(default='default.jpg', upload_to='/users_profile_images')
    about = models.TextField()

    def __str__(self):
        return self.user.username