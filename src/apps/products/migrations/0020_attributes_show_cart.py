# Generated by Django 4.2.3 on 2023-09-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributes',
            name='show_cart',
            field=models.BooleanField(default=False, verbose_name='Kartın üstünə gəldikdə göstərilsin'),
        ),
    ]
