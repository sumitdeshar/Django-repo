# Generated by Django 4.1.4 on 2023-01-11 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='features',
            name='details',
            field=models.CharField(default=100, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='name',
            field=models.CharField(default=500, max_length=100),
            preserve_default=False,
        ),
    ]
