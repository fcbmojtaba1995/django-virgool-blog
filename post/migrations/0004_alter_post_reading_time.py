# Generated by Django 3.2.5 on 2021-07-24 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reading_time',
            field=models.PositiveSmallIntegerField(verbose_name='reading time'),
        ),
    ]