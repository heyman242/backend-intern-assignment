# Generated by Django 4.2.2 on 2023-06-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('Incomplete', 'Incomplete'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=20)),
            ],
        ),
    ]
