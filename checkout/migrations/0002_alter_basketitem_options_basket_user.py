# Generated by Django 4.0.7 on 2022-09-03 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basketitem',
            options={'verbose_name': 'Basket Item', 'verbose_name_plural': 'Basket Items'},
        ),
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='basketofuser', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
