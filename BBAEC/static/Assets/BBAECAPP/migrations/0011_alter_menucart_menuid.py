# Generated by Django 5.0.4 on 2024-04-29 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBAECAPP', '0010_menucart_banqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucart',
            name='menuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BBAECAPP.menu', verbose_name='Menu'),
        ),
    ]