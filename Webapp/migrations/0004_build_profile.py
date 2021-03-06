# Generated by Django 2.2.16 on 2020-12-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0003_delete_build_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuilD_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('DOB', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
