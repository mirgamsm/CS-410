# Generated by Django 3.2.8 on 2021-11-19 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0010_alter_tutor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name=''),
        ),
    ]
