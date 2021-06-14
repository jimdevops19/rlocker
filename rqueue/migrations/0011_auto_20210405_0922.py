# Generated by Django 3.1.2 on 2021-04-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rqueue", "0010_auto_20210404_1102"),
    ]

    operations = [
        migrations.DeleteModel(
            name="FinishedQueue",
        ),
        migrations.AddField(
            model_name="rqueue",
            name="description",
            field=models.CharField(
                blank=True, default=None, max_length=2048, null=True
            ),
        ),
    ]
