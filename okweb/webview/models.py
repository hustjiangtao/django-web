from django.db import models

# Create your models here.


class Website(models.Model):
    website_name = models.CharField(max_length=64)
    website_url = models.CharField(max_length=255)
    website_create_time = models.DateTimeField(auto_now_add=True)
