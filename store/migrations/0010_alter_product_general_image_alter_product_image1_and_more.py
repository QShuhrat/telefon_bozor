# Generated by Django 4.1.1 on 2022-09-18 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_general_image_alter_product_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='General_image',
            field=models.ImageField(blank=True, default='./f74f39dbc9b60954c926d72401adf1cc.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, default='./f74f39dbc9b60954c926d72401adf1cc.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, default='./f74f39dbc9b60954c926d72401adf1cc.jpg', null=True, upload_to=''),
        ),
    ]
