# Generated by Django 4.1 on 2023-06-12 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finalapp", "0011_salesperson_sarr_salesperson_sle"),
    ]

    operations = [
        migrations.CreateModel(
            name="EXM",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("MID", models.CharField(max_length=20)),
                ("MNAME", models.CharField(max_length=100, null=True)),
                ("MFuction", models.CharField(max_length=100, null=True)),
                ("EXMAmount", models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name="branch",
            name="SMON",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="branch", name="SNSALE", field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="branch", name="SNew", field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="branch", name="SOSALE", field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="branch", name="SOld", field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="branch", name="STc", field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="BID",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="CGender",
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="CHow",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="CMON",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="massagechair",
            name="MFuction",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="massagechair",
            name="MNAME",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="purchase",
            name="MFuction",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="purchase",
            name="MNAME",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="purchase", name="PDdate", field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="salesdetail",
            name="CAge_range",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="salesdetail",
            name="MNAME",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="branch", name="SAc", field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="massagechair", name="MState", field=models.BooleanField(),
        ),
    ]
