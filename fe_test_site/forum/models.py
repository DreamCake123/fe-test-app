from django.db import models

# Create your models here.
class Post(models.Model):
    post_text = models.CharField(max_length=1024)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.post_text

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=512)
    def __str__(self):
        return self.comment_text