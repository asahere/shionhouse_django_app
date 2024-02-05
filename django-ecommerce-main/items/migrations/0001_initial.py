# Generated by Django 4.2.7 on 2023-11-24 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=30)),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Item",
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
                ("title", models.CharField(max_length=60)),
                ("description", models.TextField()),
                ("price", models.FloatField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="item_images"),
                ),
                ("is_sold", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Purchase",
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
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="items.item"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="item",
            name="buyers",
            field=models.ManyToManyField(
                related_name="purchased_items",
                through="items.Purchase",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="item",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="items.category",
            ),
        ),
    ]