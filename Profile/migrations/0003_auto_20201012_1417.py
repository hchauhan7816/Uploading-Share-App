# Generated by Django 3.1 on 2020-10-12 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_auto_20201011_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_pic',
            field=models.ImageField(default='avatar.png', upload_to='profile_pic'),
        ),
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
