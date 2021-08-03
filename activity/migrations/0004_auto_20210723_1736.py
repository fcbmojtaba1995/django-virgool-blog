# Generated by Django 3.2.5 on 2021-07-23 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_relation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_time',), 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='relation',
            options={'ordering': ('-created_time',), 'verbose_name': 'Relation', 'verbose_name_plural': 'Relations'},
        ),
        migrations.AlterModelTable(
            name='comment',
            table='comment',
        ),
        migrations.AlterModelTable(
            name='relation',
            table='relation',
        ),
    ]
