from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    topic = models.CharField(max_length=60, unique=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic

    def __repr__(self):
        return f"{self.topic}, {self.pub_date}, {self.creator}"


class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"comment by {self.creator}"




    


