# Generated by Django 2.2.28 on 2022-11-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigItem',
            fields=[
                ('key', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
    ]
