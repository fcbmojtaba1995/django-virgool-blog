# Generated by Django 3.2.5 on 2021-07-22 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20210718_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/account/user_avatar/', verbose_name='avatar'),
        ),
    ]
