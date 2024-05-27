# Generated by Django 5.0.3 on 2024-05-09 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBAECAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('package', models.IntegerField()),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
        migrations.AddField(
            model_name='banquet',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Available'),
        ),
        migrations.CreateModel(
            name='dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.FloatField()),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
                ('mid', models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.CASCADE, to='BBAECAPP.menu')),
            ],
        ),
    ]