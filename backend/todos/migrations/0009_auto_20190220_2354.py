# Generated by Django 2.1.7 on 2019-02-21 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0008_auto_20190220_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
