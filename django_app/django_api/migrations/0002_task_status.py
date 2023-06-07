# Generated by Django 4.2.2 on 2023-06-07 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('INITIATED', 'Initiated'), ('PENDING', 'Pending'), ('COMPLETED', 'Completed')], default='PENDING', max_length=10),
        ),
    ]