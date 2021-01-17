from django import forms 
from django.contrib.auth.models import User
from .models import *
  
class PhotoForm(forms.ModelForm): 
  
    class Meta: 
        model = photo
        fields = ['img','caption','user'] 