# Generated by Django 3.2.8 on 2021-11-09 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0007_alter_tutor_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='abilitiesquestion',
            field=models.TextField(blank=True, max_length=1500, verbose_name='How Would You Address A Range Of Abilities In Your Classroom: (200 Words or Less)'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='introduction',
            field=models.TextField(blank=True, max_length=1500, verbose_name='Introduction (Describe Yourself in 200 Words or Less)'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='teachercharacteristics',
            field=models.TextField(blank=True, max_length=1500, verbose_name='What Characteristics Make A Good Teacher: (200 Words or Less)'),
        ),
    ]
