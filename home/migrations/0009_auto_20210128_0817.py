# Generated by Django 3.0.6 on 2021-01-28 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210127_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img1',
            field=models.ImageField(upload_to='prod_imgs/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img2',
            field=models.ImageField(upload_to='prod_imgs/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img3',
            field=models.ImageField(upload_to='prod_imgs/'),
        ),
    ]
