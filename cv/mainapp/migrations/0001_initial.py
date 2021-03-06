# Generated by Django 2.1.2 on 2019-03-19 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddEducationTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256, verbose_name='Описание курсов')),
                ('image', models.ImageField(blank=True, upload_to='add_education_images')),
                ('dates', models.CharField(max_length=64, verbose_name='Год обучения')),
            ],
        ),
        migrations.CreateModel(
            name='CareerTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Место работы')),
                ('position', models.CharField(max_length=128, verbose_name='Должность')),
                ('image', models.ImageField(blank=True, upload_to='career_images')),
                ('dates', models.CharField(max_length=64, verbose_name='Стаж работы')),
            ],
        ),
        migrations.CreateModel(
            name='CertificatesTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название курса')),
                ('image', models.ImageField(blank=True, upload_to='add_education_images')),
            ],
        ),
        migrations.CreateModel(
            name='EducationTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название ОУ')),
                ('image', models.ImageField(blank=True, upload_to='education_images')),
                ('dates', models.CharField(max_length=64, verbose_name='Годы обучения')),
            ],
        ),
        migrations.CreateModel(
            name='MenuCategoryTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Название пункта меню')),
            ],
        ),
        migrations.AddField(
            model_name='educationtable',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.MenuCategoryTable'),
        ),
        migrations.AddField(
            model_name='certificatestable',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.MenuCategoryTable'),
        ),
        migrations.AddField(
            model_name='careertable',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.MenuCategoryTable'),
        ),
        migrations.AddField(
            model_name='addeducationtable',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.MenuCategoryTable'),
        ),
    ]
