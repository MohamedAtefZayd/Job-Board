# Generated by Django 3.0.8 on 2020-07-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_auto_20200712_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='Deadline',
            field=models.DateTimeField(help_text='Example : 2002-12-29'),
        ),
    ]
