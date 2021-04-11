from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(
        upload_to="blog/images", blank=True, null=True)
    category = models.CharField(max_length=150)
    description = RichTextField()
    published = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        global str
        if self.slug == None:
            slug = slugify(self.title)

            has_slug = Blog.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.slug) + '-' + str(count)
                has_slug = Blog.objects.filter(slug=slug).exists()
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    post = models.ForeignKey(
        Blog, on_delete=models.SET_NULL, null=True, related_name='comments')
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    approved = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
