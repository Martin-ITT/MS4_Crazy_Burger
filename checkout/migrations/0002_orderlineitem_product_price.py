# Generated by Django 3.2.6 on 2021-09-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='product_price',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=6),
            preserve_default=False,
        ),
    ]
