# Generated by Django 5.1.2 on 2025-01-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='expirationDateTime',
            field=models.CharField(default='01.10.2000 00:00:15', max_length=70, verbose_name='Время жизни токена'),
        ),
    ]
