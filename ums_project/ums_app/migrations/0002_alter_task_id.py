# Generated by Django 4.2.2 on 2023-06-08 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ums_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
