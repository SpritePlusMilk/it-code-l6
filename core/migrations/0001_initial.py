# Generated by Django 4.2 on 2023-04-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('position', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
    ]