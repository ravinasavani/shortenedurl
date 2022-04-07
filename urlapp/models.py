from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UrlData(models.Model):
    url = models.CharField(max_length=200)
    slug = models.CharField(max_length=15)
    user = models.ForeignKey(to = User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"Short Url for: {self.url} is {self.slug}"

