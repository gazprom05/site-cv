# Generated by Django 2.1.2 on 2019-03-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificatestable',
            name='image',
            field=models.ImageField(blank=True, upload_to='certificate_images'),
        ),
    ]
