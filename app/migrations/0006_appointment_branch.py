# Generated by Django 5.0.4 on 2024-04-18 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_order_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.branch'),
            preserve_default=False,
        ),
    ]