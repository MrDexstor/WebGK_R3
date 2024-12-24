from django.db import models
from Core.models import User 


class Warehouse(models.Model):
    name = models.CharField('Наименование склада',max_length=255)

    def __str__(self):
        return self.name

class Shelf(models.Model):
    number = models.CharField('Номер полки', max_length=50)
    name = models.CharField('Наименование  полки', max_length=255)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='shelves')

    def __str__(self):
        return f"{self.name} (Полка № {self.number})"

class Product(models.Model):
    plu = models.CharField('PLU', max_length=50, unique=False)
    name = models.CharField('Наименованеи', max_length=255)
    stock_on_shelf = models.IntegerField('Остаток на полке')
    global_stock = models.IntegerField('Остаток в GK')
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, related_name='products')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='products')

    class Meta:
        unique_together = ('shelf', 'warehouse', 'plu')

    def __str__(self):
        return self.name


class Inventory(models.Model):
    STATUS_CHOICES = [
        ('open', 'Открыта'),
        ('closed', 'Закрыта'),
    ]
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='inventories')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventories')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return f"Inventory {self.id} for {self.warehouse.name}"

class InventoryItem(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('processed', 'Обработано'),
    ]
    plu = models.CharField('PLU', max_length=50)
    name = models.CharField('Наименование', max_length=255)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='items')
    quantity_to_display = models.IntegerField('Количество к выкладке', null=True, blank=True)
    status = models.CharField('Статус обработки', max_length=10, choices=STATUS_CHOICES, default='pending')
    total_stock = models.IntegerField('Суммарный остаток на складе')

    def __str__(self):
        return f"{self.name} (PLU: {self.plu})"
