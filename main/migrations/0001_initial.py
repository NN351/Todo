# Generated by Django 3.1.3 on 2021-01-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
