# Generated by Django 5.1.2 on 2025-01-14 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='expirationDateTime',
        ),
        migrations.AddField(
            model_name='user',
            name='expirationDateTim',
            field=models.CharField(default='01.10.2000 00:00:15', max_length=70, verbose_name='Время жизни токена'),
        ),
    ]
