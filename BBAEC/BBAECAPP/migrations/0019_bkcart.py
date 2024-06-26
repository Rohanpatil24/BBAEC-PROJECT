# Generated by Django 5.0.6 on 2024-05-25 14:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBAECAPP', '0018_morder_bid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='bkcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50)),
                ('qty', models.IntegerField(default=1)),
                ('bid', models.ForeignKey(db_column='bid', default=9, on_delete=django.db.models.deletion.CASCADE, to='BBAECAPP.banquet')),
                ('mid', models.ForeignKey(db_column='mid', default=9, on_delete=django.db.models.deletion.CASCADE, to='BBAECAPP.menu')),
                ('uid', models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
