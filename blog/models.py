from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)

    slug = models.SlugField(null=True, unique=True)

    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('post_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)