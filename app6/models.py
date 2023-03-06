from django.db import models

# Create your models here.
class Register(models.Model):
    Name=models.CharField(max_length=10)
    Age=models.IntegerField()
    Place=models.CharField(max_length=10)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)

class Images(models.Model):
    Name=models.CharField(max_length=10)
    Age=models.IntegerField()
    Place=models.CharField(max_length=10)
    Image=models.ImageField(upload_to='media/',null=True,blank=True)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)


