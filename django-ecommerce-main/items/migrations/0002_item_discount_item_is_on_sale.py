# Generated by Django 4.2.7 on 2023-11-24 16:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="discount",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="item",
            name="is_on_sale",
            field=models.BooleanField(default=False),
        ),
    ]
