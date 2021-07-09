from django.db import models
from django.db.models.base import Model

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)

    def seralize(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "email": self.email,
            "password":self.password
        }