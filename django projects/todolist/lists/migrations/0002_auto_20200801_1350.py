# Generated by Django 3.0.8 on 2020-08-01 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='full_note',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
