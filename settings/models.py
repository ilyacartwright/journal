from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField



class Schools(models.Model):
    full_name = models.CharField(_('Полное название'), max_length=128)
    short_name = models.CharField(_('Сокращенное название'), max_length=8)
    number = models.IntegerField(_('Номер (если есть)'), blank=True, null=True)
    address = models.CharField(_('Адрес'), max_length=128)
    phone = PhoneNumberField(_('Номер телефона:'), null=False, blank=False, unique=True)

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'

    def __str__(self):
        return self.full_name
    

class Positions(models.Model):
    name = models.CharField(_("Название"), max_length=50)

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        return self.name
