# Generated by Django 5.0.4 on 2024-05-07 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BBAECAPP', '0013_menucart_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menucart',
            name='menuid',
        ),
    ]
