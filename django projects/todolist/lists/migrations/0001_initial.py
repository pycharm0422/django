# Generated by Django 3.0.8 on 2020-08-01 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_note', models.CharField(max_length=20, null=True)),
                ('full_note', models.CharField(max_length=200, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
