# Generated by Django 3.1.2 on 2021-04-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lockable_resource', '0005_auto_20210406_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='lockableresource',
            name='link',
            field=models.CharField(blank=True, default=None, max_length=2048, null=True),
        ),
    ]
