# Generated by Django 5.1.6 on 2025-02-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_citizen_phone_number_alter_institute_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='address',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='blood_type',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='city',
            field=models.CharField(choices=[('Amman', 'Amman'), ('Irbid', 'Irbid'), ('Aqaba', 'Aqaba')], max_length=10),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='phone_number',
            field=models.CharField(default='0000000000', max_length=15, unique=True),
        ),
    ]
