# Generated by Django 5.0 on 2024-10-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="bathrooms",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="property",
            name="bedrooms",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="property",
            name="guests",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="property",
            name="price_per_night",
            field=models.IntegerField(default=1),
        ),
    ]