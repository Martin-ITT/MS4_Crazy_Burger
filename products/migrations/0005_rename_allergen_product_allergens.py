# Generated by Django 3.2.6 on 2021-09-04 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210904_0923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='allergen',
            new_name='allergens',
        ),
    ]
