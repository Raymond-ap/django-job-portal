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
    thumbnail = models.ImageField(upload_to='jobs_img', blank=True, null=True)
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

    # Generate random slugs
    def save(self, *args, **kwargs):
        global str
        if self.slug == None:
            slug = slugify(self.job_title)

            has_slug = Job.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.slug) + '-' + str(count)
                has_slug = Job.objects.filter(slug=slug).exists()
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.company_name


class JobRequirement(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE,
                            related_name='requirements')
    requirement = models.CharField(max_length=1000)

    def __str__(self):
        return f'Requirements for {self.job.job_title}'
