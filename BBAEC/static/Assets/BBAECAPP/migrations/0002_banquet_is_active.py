# Generated by Django 5.0.4 on 2024-04-25 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBAECAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banquet',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Available'),
        ),
    ]
