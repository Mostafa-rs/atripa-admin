# Generated by Django 4.2.3 on 2023-07-19 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0016_accommodation_deleted_bank_deleted_company_deleted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='continental',
            name='english_name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
