# Generated by Django 2.2.5 on 2020-05-05 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0002_auto_20200505_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airports_arr',
            name='IACO',
            field=models.CharField(max_length=4, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='airports_arr',
            name='airport_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='airports_arr',
            name='lat',
            field=models.FloatField(unique=True),
        ),
        migrations.AlterField(
            model_name='airports_arr',
            name='lon',
            field=models.FloatField(unique=True),
        ),
        migrations.AlterField(
            model_name='airports_dep',
            name='IACO',
            field=models.CharField(max_length=4, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='airports_dep',
            name='airport_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='airports_dep',
            name='lat',
            field=models.FloatField(unique=True),
        ),
        migrations.AlterField(
            model_name='airports_dep',
            name='lon',
            field=models.FloatField(unique=True),
        ),
    ]
