# Generated by Django 3.2.4 on 2021-06-29 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='csv_files')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_board', models.CharField(max_length=150)),
                ('allcategory_boys', models.CharField(max_length=150)),
                ('allcategory_girls', models.CharField(max_length=150)),
                ('allcategory_total', models.CharField(max_length=150)),
                ('allcategory_passed_boys', models.CharField(max_length=150)),
                ('allcategory_passed_girls', models.CharField(max_length=150)),
                ('allcategory_passed_total', models.CharField(max_length=150)),
                ('schedulecaste_boys', models.CharField(max_length=150)),
                ('schedulecaste_girls', models.CharField(max_length=150)),
                ('schedulecaste_total', models.CharField(max_length=150)),
                ('schedulecaste_passed_boys', models.CharField(max_length=150)),
                ('schedulecaste_passed_girls', models.CharField(max_length=150)),
                ('schedulecaste_passed_total', models.CharField(max_length=150)),
                ('scheduletribe_boys', models.CharField(max_length=150)),
                ('scheduletribe_girls', models.CharField(max_length=150)),
                ('scheduletribe_total', models.CharField(max_length=150)),
                ('scheduletribe_passed_boys', models.CharField(max_length=150)),
                ('scheduletribe_passed_girls', models.CharField(max_length=150)),
                ('scheduletribe_passed_total', models.CharField(max_length=150)),
            ],
        ),
    ]
