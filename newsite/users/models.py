from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #for ImageField need install Pillow package
    img = models.ImageField(default = 'default-image.png', upload_to = 'user_images')

    def __str__(self):
        return 'Профиль пользователя %s' % self.user.username
