# Generated by Django 2.2.16 on 2020-12-27 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0004_build_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build_profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
