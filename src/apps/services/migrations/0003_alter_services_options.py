# Generated by Django 4.2.3 on 2023-08-05 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_services_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
    ]
