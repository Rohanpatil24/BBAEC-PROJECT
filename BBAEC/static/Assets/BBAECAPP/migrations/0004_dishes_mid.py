# Generated by Django 5.0.4 on 2024-04-25 07:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBAECAPP', '0003_dishes_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishes',
            name='mid',
            field=models.ForeignKey(db_column='mid', default=0, on_delete=django.db.models.deletion.CASCADE, to='BBAECAPP.menu'),
            preserve_default=True,
        ),
    ]