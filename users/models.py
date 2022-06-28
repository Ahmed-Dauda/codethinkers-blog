from django.db import models
from django.contrib.auth.models import User

# class Profile(models.Model):
#     owner = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')

#     def __str__(self):
#         return f"{self.owner.username} Profile"
        
