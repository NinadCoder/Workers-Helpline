# Generated by Django 5.1.7 on 2025-03-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('worker', 'Worker'), ('hirer', 'Hirer')], default='hirer', max_length=10),
        ),
    ]
