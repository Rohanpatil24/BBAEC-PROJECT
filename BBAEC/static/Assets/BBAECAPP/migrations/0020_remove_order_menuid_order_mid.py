# Generated by Django 5.0.4 on 2024-05-07 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBAECAPP', '0019_remove_order_mid_order_menuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='menuid',
        ),
        migrations.AddField(
            model_name='order',
            name='mid',
            field=models.ForeignKey(db_column='mid', default=1, on_delete=django.db.models.deletion.CASCADE, to='BBAECAPP.menu'),
            preserve_default=False,
        ),
    ]
