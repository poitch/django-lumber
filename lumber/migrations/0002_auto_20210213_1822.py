# Generated by Django 3.1.6 on 2021-02-14 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lumber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='thread',
            field=models.PositiveBigIntegerField(blank=True, default=None, null=True),
        ),
    ]
