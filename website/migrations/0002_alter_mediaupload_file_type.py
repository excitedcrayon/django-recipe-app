# Generated by Django 5.0 on 2023-12-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediaupload',
            name='file_type',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
