# Generated by Django 4.2.4 on 2023-10-02 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0008_post_latitud_post_longitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='latitud',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='longitud',
            field=models.CharField(max_length=50),
        ),
    ]
