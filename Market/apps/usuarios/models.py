from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    dni = models.IntegerField(null=True, blank=True)
        
    def __str__(self):
        return self.get_full_name()
    class Meta:
        db_table = "usuarios"
    # foto = models.ImageField()
