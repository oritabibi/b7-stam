# Generated by Django 3.0.4 on 2020-03-26 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_gardens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doggarden',
            name='street',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
