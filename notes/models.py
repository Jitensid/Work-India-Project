from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Note(models.Model):
	text = models.TextField(blank=False)
	author = models.ForeignKey(User, on_delete=models.CASCADE)#if a user is deleted than we delete all the posts made by that user
	posted_on = models.DateTimeField(default=timezone.now)