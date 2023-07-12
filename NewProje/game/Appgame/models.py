from django.db import models
from django.contrib.auth.models import User

class Userinfo(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    password = models.CharField(("Parola"), max_length=50)
    profilimg = models.ImageField(("Profil Fotoğrafı"), upload_to="ProfilFotoğrafları", default="person.png")
