# Generated by Django 4.1.5 on 2023-02-10 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Health', '0004_predict_are_you_above_60_predict_fever_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predict',
            name='patient',
        ),
    ]