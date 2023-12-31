# Generated by Django 4.2.3 on 2023-08-06 10:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_contact_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255, verbose_name='telefon')),
                ('facebook_url', models.URLField(max_length=500)),
                ('tiktok_url', models.URLField(max_length=500)),
                ('instagram_url', models.URLField(max_length=500)),
                ('about_company', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='haqqımızda')),
            ],
        ),
    ]
