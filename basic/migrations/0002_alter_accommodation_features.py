# Generated by Django 4.2.3 on 2023-08-07 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='features',
            field=models.ManyToManyField(blank=True, related_name='ba_features', to='basic.accommodationfeature'),
        ),
    ]