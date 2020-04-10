# Generated by Django 3.0.4 on 2020-04-10 12:07

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0005_auto_20200403_1832'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'Basket', 'verbose_name_plural': 'Baskets'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
        migrations.AlterModelOptions(
            name='requesterror',
            options={'ordering': ('-created_at',), 'verbose_name': 'Request Error', 'verbose_name_plural': 'Request Errors'},
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='', verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basket',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='basketitem',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.Basket', verbose_name='Basket'),
        ),
        migrations.AlterField(
            model_name='basketitem',
            name='count',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Count'),
        ),
        migrations.AlterField(
            model_name='basketitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='subcategories',
            field=models.ManyToManyField(blank=True, related_name='_category_subcategories_+', to='shop.Category', verbose_name='Subcategories'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=20, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Basket', verbose_name='Basket'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('waiting', 'Waiting'), ('processing', 'Processing'), ('processed', 'Processed')], default='waiting', max_length=10, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='shop.Category', verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='value',
            field=models.PositiveIntegerField(verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image_base64',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Image base64'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.Product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='requesterror',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='requesterror',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='requesterror',
            name='exception_name',
            field=models.CharField(max_length=50, verbose_name='Exception name'),
        ),
        migrations.AlterField(
            model_name='requesterror',
            name='exception_tb',
            field=models.TextField(verbose_name='Exception tb'),
        ),
        migrations.AlterField(
            model_name='requesterror',
            name='exception_value',
            field=models.CharField(max_length=250, verbose_name='Exception value'),
        ),
        migrations.AlterField(
            model_name='requesterror',
            name='path',
            field=models.CharField(max_length=500, verbose_name='Path'),
        ),
        migrations.AlterField(
            model_name='requesterror',
            name='query',
            field=django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Query'),
        ),
        migrations.AlterField(
            model_name='requesterror',
            name='request_method',
            field=models.CharField(max_length=10, verbose_name='Request method'),
        ),
    ]
