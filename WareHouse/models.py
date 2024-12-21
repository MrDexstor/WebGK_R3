from django.db import models

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
        unique_together = ('shelf', 'warehouse')

    def __str__(self):
        return self.name
