# Generated by Django 5.0.4 on 2024-05-07 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBAECAPP', '0018_alter_order_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='mid',
        ),
        migrations.AddField(
            model_name='order',
            name='menuid',
            field=models.ForeignKey(db_column='menuid', default=1, on_delete=django.db.models.deletion.CASCADE, to='BBAECAPP.foodcart'),
            preserve_default=False,
        ),
    ]
