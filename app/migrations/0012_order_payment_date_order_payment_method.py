# Generated by Django 5.0.4 on 2024-04-28 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_gallery_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_date',
            field=models.CharField(default=1, max_length=128, verbose_name='Created At'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default=1, max_length=128, verbose_name='Payment method'),
            preserve_default=False,
        ),
    ]
