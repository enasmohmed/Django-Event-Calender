from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    date = models.DateField()



    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('event:event_detail', args=(self.pk,))