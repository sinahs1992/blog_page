# Generated by Django 4.2.8 on 2023-12-30 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
