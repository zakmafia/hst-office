# Generated by Django 5.0.3 on 2024-04-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hst_IT_asset_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptopstore',
            name='storage',
            field=models.IntegerField(verbose_name='Storage in GB'),
        ),
    ]