# Generated by Django 4.2.1 on 2023-07-14 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='waiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Age', models.PositiveIntegerField()),
                ('Phone', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=300)),
            ],
        ),
    ]
