# Generated by Django 4.2.3 on 2023-08-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_attributes_product_attributes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='attributes',
            field=models.ManyToManyField(related_name='products', to='products.attributes'),
        ),
    ]
