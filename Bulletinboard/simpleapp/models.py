from django.db import models
from Bulletin.models import Post
from django.contrib.auth.models import User

class Replies(models.Model):
    textreply = models.TextField(default="reply")
    replyfrom = models.ForeignKey(User, on_delete=models.CASCADE)
    replyto = models.ForeignKey(Post, on_delete=models.CASCADE)
    isaccepted = models.BooleanField(default=False)

    def __str__(self):
        return self.textreply
    
    def get_absolute_url(self):
        return f'/myreply'

class AcceptReply(models.Model):
    replies = models.ForeignKey(Replies, on_delete=models.CASCADE)

    def __str__(self):
        return self.replies.textreply

    def get_absolute_url(self):
        return f'/{self.id}'