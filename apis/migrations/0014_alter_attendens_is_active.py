# Generated by Django 4.2.16 on 2024-11-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0013_alter_users_telegram_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendens',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
