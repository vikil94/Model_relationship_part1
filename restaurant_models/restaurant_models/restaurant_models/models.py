from django.db import models

class Publication(models.Model):
    name = models.CharField(max_length=255)

class Critic(models.Model):
    name = models.CharField(max_length=255)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='publication')

class Restaurant(models.Model):
    name = models.CharField(max_length=255)

class Chef(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Review(models.Model):
    title = models.CharField(max_length=255)
    review = models.TextField()
    critic = models.ForeignKey(Critic, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
              
