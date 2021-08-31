from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE, null = False, blank = True)

    profile_image = models.ImageField('Profile Image', null = True, blank = True)

    bio = models.TextField('Bio', null = True, blank = True)

    phone = models.CharField('Mobile No', max_length = 225, null = True, blank = True)
    
    nickname = models.CharField('Nickname', max_length = 225, null = True, blank = True)

    location = models.CharField('Location', max_length = 1000, null = True, blank = True)   

    facebook = models.CharField('Facebook Link', max_length = 225, null = True, blank = True)
    
    twitter = models.CharField('Twitter Link', max_length = 225, null = True, blank = True)
    
    instagram = models.CharField('Instagram Link', max_length = 225, null = True, blank = True)
    
    linkedin = models.CharField('LinkedIn Link', max_length = 225, null = True, blank = True)
    
    youtube = models.CharField('Youtube Link', max_length = 225, null = True, blank = True)
    
    updated_at = models.DateTimeField(auto_now=True)
    


    def __str__(self) -> str:
        return f'{self.user} profile created'


