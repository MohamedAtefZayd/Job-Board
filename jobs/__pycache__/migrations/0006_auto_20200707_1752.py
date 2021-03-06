# Generated by Django 3.0.8 on 2020-07-07 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20200707_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply_job',
            name='apply_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='jobs.job'),
        ),
        migrations.AlterField(
            model_name='apply_job',
            name='cv',
            field=models.FileField(upload_to='apply/'),
        ),
        migrations.AlterField(
            model_name='apply_job',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
