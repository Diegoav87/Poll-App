from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    option_one = models.CharField(max_length=50)
    option_two = models.CharField(max_length=50)
    option_three = models.CharField(max_length=50)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='polls')
    vote_total = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("polls:all")
    
    def __str__(self):
        return self.question

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count
    