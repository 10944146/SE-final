# Generated by Django 4.1 on 2023-06-10 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finalapp", "0009_alter_salesperson_sr"),
    ]

    operations = [
        migrations.AddField(
            model_name="salesperson", name="SM1", field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="salesperson", name="SM2", field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="salesperson", name="SM3", field=models.IntegerField(null=True),
        ),
    ]
