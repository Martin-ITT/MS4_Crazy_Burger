# Generated by Django 3.2.6 on 2021-09-30 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20210930_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='strtipe_pid',
            new_name='stripe_pid',
        ),
        migrations.AlterField(
            model_name='order',
            name='original_bag',
            field=models.TextField(default=''),
        ),
    ]
