# Generated by Django 4.2.3 on 2023-08-05 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0003_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='sent_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]