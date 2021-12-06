# Generated by Django 3.2.8 on 2021-12-06 21:43

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0015_alter_tutor_phonicsex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='education',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('College Student', 'Currently Enrolled In College'), ('A.A./A.S.', "Associate's Degree"), ('Technical Certification', 'Technical Certification'), ('B.A./B.S.', "Bachelor's Degree"), ('M.A./M.S./M.Ed.', "Master's Degree"), ('Ed.S.', 'Education Specialist/6th Year/Etc . . .'), ('Ed.D./Ph.D.', 'Doctorate')], max_length=93, verbose_name='Level of Education (Please Select All That Apply):'),
        ),
    ]
