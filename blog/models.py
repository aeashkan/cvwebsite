from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog/', default='blog/defualt.jpg')
    content = models.TextField()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_date = jmodels.jDateTimeField(auto_now_add=True)
    updated_date = jmodels.jDateTimeField(auto_now=True)
    published_date = jmodels.jDateTimeField(null=True, blank=True)
    category = models.ManyToManyField(Category)
    tags = TaggableManager()

    objects = jmodels.jManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']


    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid': self.id})
