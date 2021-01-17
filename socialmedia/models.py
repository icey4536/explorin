from django.db import models
from django.contrib.auth.models import User



# Create your models here.
# models.py 
class photo(models.Model): 
	caption= models.TextField(max_length=50) 
	img = models.ImageField(upload_to='media/')
	likes = models.IntegerField(default=0)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts') 
