# Generated by Django 3.1.2 on 2021-03-01 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lockable_resource", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="lockableresource",
            options={"verbose_name_plural": "Lockable Resources"},
        ),
        migrations.AlterField(
            model_name="lockableresource",
            name="signoff",
            field=models.CharField(
                blank=True, default=None, max_length=2048, null=True
            ),
        ),
    ]
