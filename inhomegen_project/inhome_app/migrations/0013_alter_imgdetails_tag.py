# Generated by Django 4.0.5 on 2024-02-01 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inhome_app', '0012_imgdetails_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgdetails',
            name='tag',
            field=models.FloatField(default='', max_length=20),
        ),
    ]
