from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

class User(AbstractUser):
    pass
class User1(models.Model):
    name=models.CharField(max_length=64)
    passw=models.CharField(max_length=64)
    hospis=models.CharField(max_length=64)
class details(models.Model):
    hn=models.CharField(max_length=64)
    addr=models.CharField(max_length=6400)
    specs=models.CharField(max_length=6400)
    cat=models.CharField(max_length=6400)
    docts=models.CharField(max_length=6400)
    conts=models.CharField(max_length=1000)
    usr=models.CharField(max_length=64)
    amb=models.CharField(max_length=64)
    beds=models.CharField(max_length=64)
    avg=models.FloatField(default=0)
    def serialize(self):
        return {
            "hn": self.hn,
            
            
            "specs": self.specs,
            "usr": self.usr,
            "conts": self.conts,
            "docts":self.docts
             
        }
class upd(models.Model):
    vc=models.CharField(max_length=64)
    avl=models.CharField(max_length=64)
    hnm=models.CharField(max_length=64)
class appt(models.Model):
    urr=models.CharField(max_length=64)
    hnme=models.CharField(max_length=64)
    patname=models.CharField(max_length=64)
    agge=models.CharField(max_length=64)
    probl=models.CharField(max_length=6400)
    datt=models.CharField(max_length=64)
class approvedapp(models.Model):
    urr1=models.CharField(max_length=64)
    hnma=models.CharField(max_length=64)
    pate=models.CharField(max_length=64)
    dat=models.CharField(max_length=64)
class rate(models.Model):
    hos=models.CharField(max_length=64)
    urr=models.CharField(max_length=64)
    raa=models.IntegerField()
  