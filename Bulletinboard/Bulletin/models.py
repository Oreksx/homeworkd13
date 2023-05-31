from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

class Category(models.Model):
    categoryname = models.CharField(max_length = 64, unique = True)

    def __str__(self):
        return self.categoryname

class Post(models.Model):
    title = models.CharField(max_length=255, default='title')
    textpost = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    video = EmbedVideoField(blank=True, null=False)
    categorypost = models.ManyToManyField(Category, through = 'PostCategory')
    datepost = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.id}'
    
    def get_category(self):
        category = self.category.all()
        for i in category:
            category = i
        return category

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.category.categoryname
    
    def get_category(self):
        return self.category.categoryname






























