from django.db import models
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
    # slug =
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.company_name
