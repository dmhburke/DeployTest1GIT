# Generated by Django 2.1.7 on 2019-04-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playername',
            name='number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
