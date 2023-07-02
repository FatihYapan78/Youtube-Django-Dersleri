from django.db import models
from django.contrib.auth.models import User

class Userinfo(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    password = models.CharField(("Parola"), max_length=50)
