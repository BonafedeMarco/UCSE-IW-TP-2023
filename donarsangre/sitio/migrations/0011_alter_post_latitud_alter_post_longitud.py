# Generated by Django 4.2.4 on 2023-10-02 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0010_alter_post_latitud_alter_post_longitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='latitud',
            field=models.CharField(default='-31.252606961483437', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='longitud',
            field=models.CharField(default='-61.49176597595215', max_length=50),
        ),
    ]
