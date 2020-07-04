from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Post(models.Model):
    D = 0
    P = 1
    STATUS = [
        (D, "Draft"),
        (P, "Publish")
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, null=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='', related_name='blog_posts')
    content = models.TextField()
    category = models.ForeignKey('blog.Category', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

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


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, null=True, unique=True)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('category_posts', kwargs=kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)