# Generated by Django 4.2.2 on 2024-01-31 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inhome_app', '0007_delete_projectdetails_imgdetails_projname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgdetails',
            name='negprompt',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='imgdetails',
            name='prompt',
            field=models.CharField(default='', max_length=500),
        ),
    ]
