# Generated by Django 5.0.4 on 2024-04-27 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBAECAPP', '0007_banquet_bimage2_banquet_bimage3'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='package',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
