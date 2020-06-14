from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    topic = models.CharField(max_length=60, unique=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.topic

    def __repr__(self):
        return f"{self.topic}, {self.pub_date}, {self.creator}"




    


