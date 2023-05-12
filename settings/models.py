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
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'

    def __str__(self):
        return self.full_name
    

class Positions(models.Model):
    name = models.CharField(_("Название"), max_length=50)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name
    
class AcademicSubjects(models.Model):
    name = models.CharField(_("Название"), max_length=50)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Учебные предметы'

    def __str__(self):
        return self.name
