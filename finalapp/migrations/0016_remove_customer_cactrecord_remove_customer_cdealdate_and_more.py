# Generated by Django 4.1 on 2023-06-13 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("finalapp", "0015_rename_pddate_purchase_pdate_remove_purchase_bid_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="customer", name="CActrecord",),
        migrations.RemoveField(model_name="customer", name="CDealdate",),
        migrations.RemoveField(model_name="customer", name="CEmail",),
        migrations.RemoveField(model_name="customer", name="CSpecial_requests",),
        migrations.RemoveField(model_name="customer", name="CStartdate",),
        migrations.RemoveField(model_name="customer", name="SID",),
    ]