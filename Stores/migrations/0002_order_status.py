# Generated by Django 3.2.9 on 2021-12-14 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='Pending', max_length=200),
        ),
    ]
