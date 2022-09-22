from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200, unique_for_date = 'publish')
    author = models.ForeignKey(User, related_name = 'blog_post', on_delete = models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 20, choices = STATUS, default = 'draft' )

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
