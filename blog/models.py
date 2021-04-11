from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(
        upload_to="blog/images", blank=True, null=True)
    category = models.CharField(max_length=150)
    description = RichTextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    approved = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.post.title
