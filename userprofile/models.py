from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField(max_length=150)
  phone = models.CharField(max_length=100)
  address = models.CharField(max_length=200)
  pix = models.ImageField(upload_to='profilepix')
  joined = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user.username
  