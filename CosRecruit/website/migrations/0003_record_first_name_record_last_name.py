# Generated by Django 4.2.9 on 2024-11-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_record_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
