# Generated by Django 5.0.2 on 2024-02-20 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Age_guesser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ageprediction',
            name='date_of_birth',
            field=models.CharField(max_length=10),
        ),
    ]
