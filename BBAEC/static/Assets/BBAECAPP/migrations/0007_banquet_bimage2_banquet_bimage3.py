# Generated by Django 5.0.4 on 2024-04-27 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBAECAPP', '0006_banquetmanager_banquet_bimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='banquet',
            name='bimage2',
            field=models.ImageField(default=0, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banquet',
            name='bimage3',
            field=models.ImageField(default=0, upload_to='images'),
            preserve_default=False,
        ),
    ]