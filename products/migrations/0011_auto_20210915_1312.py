# Generated by Django 3.2.6 on 2021-09-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210914_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='has_toppings',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='products.Topping'),
        ),
    ]