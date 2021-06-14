# Generated by Django 3.1.2 on 2021-03-21 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rqueue", "0004_auto_20210318_2255"),
    ]

    operations = [
        migrations.CreateModel(
            name="FinishedQueue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pended_time", models.DateTimeField()),
                (
                    "rqueue",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT, to="rqueue.rqueue"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Finished Queues",
            },
        ),
    ]
