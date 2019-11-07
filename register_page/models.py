from django.db import models


from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    username = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    password1 = models.IntegerField
    password2 = models.IntegerField



# (verbose_name='شماره دانشجویی')