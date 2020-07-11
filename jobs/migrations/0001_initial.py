# Generated by Django 3.0.8 on 2020-07-04 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jobs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('low_salary', models.PositiveIntegerField(default=0)),
                ('heigh_salary', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(upload_to=jobs.models.images_upload)),
                ('vacancy', models.PositiveIntegerField(default=0)),
                ('Experience', models.PositiveIntegerField(default=0)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Any', 'Any')], max_length=50)),
                ('Deadline', models.DateField()),
                ('description', models.TextField(max_length=2000)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Country')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]