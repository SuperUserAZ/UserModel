from django.db import models
# Create your models here.

class userData(models.Model):
    user_name = models.CharField('name', max_length=20)
    user_last_name = models.CharField('lastName', max_length=20)
    user_email = models.EmailField('email', max_length=30)
    user_password = models.CharField('password', max_length=15)


    def __srt__(self):
        return self.user_name + ' ' + self.user_last_name
