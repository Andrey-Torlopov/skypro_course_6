# Generated by Django 3.2.6 on 2023-04-12 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
