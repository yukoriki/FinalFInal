# Generated by Django 4.2.9 on 2024-11-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
