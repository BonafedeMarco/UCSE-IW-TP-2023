# Generated by Django 4.2.4 on 2023-09-02 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liters_required',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='blood_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'A+'), (1, 'A-'), (2, 'B+'), (3, 'B-'), (4, 'AB+'), (5, 'AB-'), (6, 'O+'), (7, 'O-')], default='0'),
        ),
    ]
