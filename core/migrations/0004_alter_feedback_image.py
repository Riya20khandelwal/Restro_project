# Generated by Django 5.1 on 2024-09-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_feedback_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='feedback/'),
        ),
    ]
