# Generated by Django 3.0.8 on 2020-07-12 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20200712_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='Deadline',
            field=models.DateField(help_text='Example : 2002-12-29'),
        ),
    ]
