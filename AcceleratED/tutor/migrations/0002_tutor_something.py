# Generated by Django 3.2.8 on 2021-11-07 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='something',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
