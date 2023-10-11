from django.db import models

# Create your models here.
class Partners(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="partners/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Team(models.Model):
    full_name =models.CharField(max_length=100)
    image =models.ImageField(upload_to="team/", blank=True, null=True)
    position =models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.full_name

class Executive_Team(models.Model):
    full_name =models.CharField(max_length=100)
    image =models.ImageField(upload_to="team/", blank=True, null=True)
    position =models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.full_name

class Services(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content =models.TextField()
    icon =models.CharField(max_length=50, blank=True, null=True)
    image =models.ImageField(upload_to='service/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

