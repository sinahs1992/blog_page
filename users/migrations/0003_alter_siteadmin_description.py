# Generated by Django 4.2.8 on 2023-12-31 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_siteadmin_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteadmin',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
