# Generated by Django 5.1.2 on 2024-12-24 21:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WareHouse', '0003_alter_product_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('status', models.CharField(choices=[('open', 'Открыта'), ('closed', 'Закрыта')], default='open', max_length=10, verbose_name='Статус')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventories', to=settings.AUTH_USER_MODEL)),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventories', to='WareHouse.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plu', models.CharField(max_length=50, verbose_name='PLU')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('quantity_to_display', models.IntegerField(blank=True, null=True, verbose_name='Количество к выкладке')),
                ('status', models.CharField(choices=[('pending', 'В ожидании'), ('processed', 'Обработано')], default='pending', max_length=10, verbose_name='Статус обработки')),
                ('total_stock', models.IntegerField(verbose_name='Суммарный остаток на складе')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='WareHouse.inventory')),
            ],
        ),
    ]