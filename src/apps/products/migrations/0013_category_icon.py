# Generated by Django 4.2.3 on 2023-08-19 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_category_subcategory_category_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='category/', verbose_name='icon'),
        ),
    ]
