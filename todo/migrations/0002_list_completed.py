# Generated by Django 4.2.5 on 2023-09-19 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]