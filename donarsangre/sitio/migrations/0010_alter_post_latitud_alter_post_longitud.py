# Generated by Django 4.2.4 on 2023-10-02 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0009_alter_post_latitud_alter_post_longitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='latitud',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='longitud',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
