# Generated by Django 4.2.4 on 2023-08-17 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LimitList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='limitproduct',
            name='limit_product_image',
            field=models.ImageField(blank=True, upload_to='limit_product_images/%Y/%m/%d'),
        ),
    ]
