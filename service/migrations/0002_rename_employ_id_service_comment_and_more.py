# Generated by Django 4.2.7 on 2023-12-26 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='employ_id',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='service',
            name='employ_name',
        ),
    ]
