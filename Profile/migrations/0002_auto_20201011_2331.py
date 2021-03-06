# Generated by Django 3.1 on 2020-10-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='person',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='pro_pics'),
        ),
    ]
