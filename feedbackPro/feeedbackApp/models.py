from django.db import models

# Create your models here.
class FeedbackData(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField()
    date = models.DateTimeField()
    loc = models.CharField(max_length=50)
    feedback = models.TextField(max_length=500)

