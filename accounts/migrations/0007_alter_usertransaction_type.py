# Generated by Django 4.2.3 on 2023-08-16 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_usertransaction_wallet_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertransaction',
            name='type',
            field=models.IntegerField(default=0, help_text='0-4 deposit   10-14 withdraw'),
        ),
    ]
