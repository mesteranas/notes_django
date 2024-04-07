from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class notes(models.Model):
    title=models.CharField(max_length=500)
    body=models.TextField(max_length=1000000)
    date=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)