# Generated by Django 5.0.4 on 2024-05-07 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBAECAPP', '0017_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='bid',
            field=models.ForeignKey(db_column='bid', on_delete=django.db.models.deletion.CASCADE, to='BBAECAPP.banquet'),
        ),
    ]
