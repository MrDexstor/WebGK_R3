from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField('Логин', unique=True, max_length=100)
    name = models.CharField(_('name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('is_active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=True)
    login_key = models.CharField('Ключ входа по бейджу', max_length=30, blank=True, unique=False)
    storeRole = models.CharField('Роль пользователя', max_length=100, default='none')
    backoffice_login = models.CharField('Ключ BackOffice', max_length= 100, default='none')
    bearer_token = models.CharField('Bearer Token пользователя', max_length=1000, default='none')
    
    # НАСТРОЙКИ ПОЛЬЗОВАТЕЛЯ
    #Принтеры
    selected_stationary_printer = models.CharField('Выбранный стационарный принтер', max_length=100, blank=True, null=True)
    selected_thermo_printer = models.CharField('Выбранный термопринтер', max_length=100, blank=True, null=True)
    selected_mobile_printer_yellow = models.CharField('Выбранный мобильный принтер с желтой бумагой', max_length=100, blank=True, null=True)
    selected_mobile_printer_white = models.CharField('Выбранный мобильный принтер с белой бумагой', max_length=100, blank=True, null=True)
    
    
    
    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    def __str__(self):
        return self.name


class ErrorLog(models.Model):
    error_text = models.CharField('Ошибка', max_length=100)
    timestamp = models.DateTimeField('Дата и время ошибки', default= timezone.now)
    
    def __str__(self):
        return f'[{self.timestamp}] {self.error_text}'
    class Meta:
        verbose_name = 'ошибку'
        verbose_name_plural = 'ошибки'
