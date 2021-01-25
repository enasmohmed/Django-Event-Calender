from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return '%s' %(self.title)



class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return str(self.user)
