# Generated by Django 3.1.7 on 2021-04-10 14:26

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=200)),
                ('company_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='jobs_img')),
                ('job_type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Internship', 'Internship')], default=1, max_length=20)),
                ('description', ckeditor.fields.RichTextField()),
                ('location', models.CharField(max_length=150)),
                ('salary', models.FloatField(blank=True, null=True)),
                ('application_url', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=True)),
                ('category', models.ForeignKey(default='Others', on_delete=django.db.models.deletion.CASCADE, to='portal.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='JobRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirement', models.CharField(max_length=1000)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='portal.job')),
            ],
        ),
    ]
