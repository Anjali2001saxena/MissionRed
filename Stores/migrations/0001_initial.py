# Generated by Django 3.2.9 on 2021-12-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('store', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('customer', models.CharField(max_length=200)),
                ('timing', models.DateTimeField(auto_now_add=True)),
                ('items', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('contact', models.CharField(max_length=50)),
                ('location', models.TextField()),
                ('pin_code', models.CharField(max_length=50)),
                ('delivery', models.BooleanField()),
                ('password', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
