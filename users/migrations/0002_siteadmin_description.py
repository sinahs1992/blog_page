# Generated by Django 4.2.8 on 2023-12-31 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteadmin',
            name='description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
