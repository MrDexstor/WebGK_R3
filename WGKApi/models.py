from django.db import models
from Core.models import User


class Files(models.Model):
    
    name = models.CharField('Наименование файла', max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/')
    type = models.CharField('Расширение файла', max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    