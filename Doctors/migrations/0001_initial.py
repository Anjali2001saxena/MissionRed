# Generated by Django 3.2.9 on 2021-12-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('contact', models.CharField(max_length=50)),
                ('specialization', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=50)),
                ('registeration_number', models.CharField(max_length=200)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slot', models.DateTimeField()),
                ('doctor', models.CharField(max_length=200)),
                ('patient', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('patient_contact', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('status', models.CharField(default='Available', max_length=200)),
            ],
        ),
    ]
