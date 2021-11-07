# Generated by Django 3.2.8 on 2021-11-07 19:31

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0004_auto_20211106_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='availability',
            field=models.CharField(blank=True, choices=[('AM', 'Part Time AM'), ('PM', 'Part Time PM'), ('F', 'Full Time (AM and PM)')], max_length=20, verbose_name='Choose Your Availability:'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='introduction',
            field=models.TextField(blank=True, verbose_name='Introduction (Describe Yourself in 200 Words or Less)'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('English', 'English'), ('Spanish', 'Spanish'), ('Chinese', 'Chinese'), ('Other', 'Other')], default='None', max_length=29, verbose_name='Languages Spoken Fluently'),
        ),
    ]
