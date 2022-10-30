# Generated by Django 4.0.7 on 2022-09-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_remove_basketitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]