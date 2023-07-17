from django.db import models
from django.contrib.auth.models import User

SUBMISSION_TYPES = [('image', 'image'), ('file', 'file'), ('link', 'link')]

# Create your models here.
class Hackathon(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    # bg_image = models.CharField(max_length=100)
    # hackathon_img = models.CharField(max_length=100)
    submission_type = models.CharField(choices=SUBMISSION_TYPES, max_length=10)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

    users = models.ManyToManyField(User)