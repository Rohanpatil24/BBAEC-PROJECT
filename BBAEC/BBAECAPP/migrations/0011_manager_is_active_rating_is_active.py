# Generated by Django 5.0.6 on 2024-05-15 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBAECAPP', '0010_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Available'),
        ),
        migrations.AddField(
            model_name='rating',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Available'),
        ),
    ]
