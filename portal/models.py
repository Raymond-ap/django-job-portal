from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

_job_Type = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
)


class Job(models.Model):
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    job_type = models.CharField(max_length=20, choices=_job_Type, default=1)
    description = RichTextField()
    location = models.CharField(max_length=150)
    salary = models.FloatField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.company_name
    
    # Generate random slugs
    def save(self, *args, **kwargs):
        global str
        if self.slug == None:
            slug = slugify(self.title)

            has_slug = Job.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.slug) + '-' + str(count)
                has_slug = Job.objects.filter(slug=slug).exists()
            self.slug = slug
        super().save(*args, **kwargs)
