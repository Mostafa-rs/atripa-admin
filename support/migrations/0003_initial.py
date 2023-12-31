# Generated by Django 4.2.3 on 2023-08-26 07:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0002_remove_subject_parent_remove_support_creator_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=45, null=True)),
                ('date_time', models.DateTimeField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('ip', models.CharField(max_length=15, null=True)),
                ('message', models.TextField(null=True)),
                ('viewed_date', models.DateTimeField(null=True)),
                ('viewer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scf_viewer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
