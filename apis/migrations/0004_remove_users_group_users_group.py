# Generated by Django 4.2.16 on 2024-11-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_alter_attendens_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='group',
        ),
        migrations.AddField(
            model_name='users',
            name='group',
            field=models.ManyToManyField(to='apis.groups'),
        ),
    ]