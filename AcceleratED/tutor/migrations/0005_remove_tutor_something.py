# Generated by Django 3.2.8 on 2021-11-08 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0004_alter_tutor_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='something',
        ),
    ]
