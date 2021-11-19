# Generated by Django 3.2.8 on 2021-11-08 05:10

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0005_remove_tutor_something'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='employercity',
            field=models.CharField(blank=True, max_length=30, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='employerstate',
            field=models.CharField(choices=[('AL', 'AL'), ('AK', 'AK'), ('AR', 'AR'), ('AZ', 'AZ'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DC', 'DC'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'), ('IA', 'IA'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('MA', 'MA'), ('MD', 'MD'), ('ME', 'ME'), ('MI', 'MI'), ('MN', 'MN'), ('MO', 'MO'), ('MS', 'MS'), ('MT', 'MT'), ('NC', 'NC'), ('NE', 'NE'), ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NV', 'NV'), ('NY', 'NY'), ('ND', 'ND'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('WA', 'WA'), ('WI', 'WI'), ('WV', 'WV'), ('WY', 'WY'), ('None', 'None')], default='None', max_length=5, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='employerzip',
            field=models.CharField(blank=True, max_length=30, verbose_name='Zip Code'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='phonenumber',
            field=phone_field.models.PhoneField(blank=True, help_text='Phone Number', max_length=31),
        ),
    ]