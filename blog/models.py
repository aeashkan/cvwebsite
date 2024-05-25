from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


