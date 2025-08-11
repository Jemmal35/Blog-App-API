from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver



class User(AbstractUser):
    id = models.BigAutoField(primary_key= True)
    phone_number = models.CharField(max_length= 15, null= True, blank= True)
    
    def __str__(self):
        return self.username
    

class UserProfile(models.Model):
    id = models.BigAutoField(primary_key= True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name= 'profile')
    bio = models.TextField(blank= True)
    location = models.CharField(max_length= 255, blank=True)
    birth_date = models.DateField(null= True, blank= True)
    profile_picture = models.ImageField(upload_to= "profile_images/", null= True, blank= True)
    
    def __str__(self):
        return f"Profile of {self.user.username}"
    

# a signal to create a user-profle authomatically when a user is created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)