# Generated by Django 4.2.4 on 2023-08-04 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=10)),
                ('product_name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('stock', models.PositiveIntegerField()),
                ('regular_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_image', models.ImageField(upload_to='product_images/')),
            ],
        ),
    ]
