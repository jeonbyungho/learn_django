# Generated by Django 4.2.7 on 2023-11-10 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_head_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='head_image',
            field=models.ImageField(blank=True, upload_to='blog/images/%Y/%m/%d'),
        ),
    ]
