# Generated by Django 4.0 on 2021-12-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_alter_taskverification_verified_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taskverification",
            name="verified_at",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
