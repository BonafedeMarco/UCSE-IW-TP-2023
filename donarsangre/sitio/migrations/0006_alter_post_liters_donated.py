# Generated by Django 4.2.4 on 2023-10-01 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0005_post_liters_donated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liters_donated',
            field=models.FloatField(default=0, max_length=models.FloatField(default=0)),
        ),
    ]
