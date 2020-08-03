from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    about = models.TextField(default='Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam iure eius excepturi at explicabo officia illum illo doloremque eligendi dolor? Sit assumenda neque optio atque, perspiciatis maiores cum expedita nostrum impedit unde quidem.')

    def __str__(self):
        return self.user.username

class Quotes(models.Model):
    quote = models.TextField()
    author_name = models.CharField(max_length=30, default='Anonymous')

    def __str__(self):
        return self.author_name