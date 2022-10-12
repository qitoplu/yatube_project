from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
        )
    group = models.ForeignKey(
        'Group',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='posts'
        )


class Group(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()

def __str__(self):
    return self.title()
