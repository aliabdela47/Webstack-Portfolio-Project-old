# Generated by Django 4.2.3 on 2023-09-16 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
