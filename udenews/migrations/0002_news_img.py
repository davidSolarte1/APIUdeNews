# Generated by Django 5.0 on 2023-12-13 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udenews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, upload_to='news/'),
        ),
    ]
