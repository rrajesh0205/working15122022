# Generated by Django 3.0.3 on 2020-04-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200425_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]
