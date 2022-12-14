# Generated by Django 4.0.7 on 2022-09-08 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_blog_comment_options_alter_categories_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productreview',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='productreview',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_reviews', to='product.product'),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='nickname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='review',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='summary',
            field=models.CharField(max_length=100),
        ),
    ]
