from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField



class Employees(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(_("Имя"), max_length=50)
    last_name = models.CharField(_("Фамилия"), max_length=50)
    surname = models.CharField(_("Отчество"), max_length=50, blank=True, null=True)
    phone = PhoneNumberField(_('Номер телефона:'), null=True, blank=True, unique=True)
    management = models.BooleanField(_("Сотрудник может иметь класное руководство?"), null=True, blank=True)


    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.surname}'

class PlaceWork(models.Model):
    employees = models.ForeignKey("Employees", verbose_name=_("Сотрудник"), on_delete=models.CASCADE)
    school = models.ManyToManyField("settings.Schools", verbose_name=_("Школа"))
    position = models.ManyToManyField("settings.Positions", verbose_name=_("Должность"))
    subject = models.ManyToManyField("settings.AcademicSubjects", verbose_name=_("Предметы:"))

class Cabinet(models.Model):
    school = models.ForeignKey("settings.Schools", verbose_name=_("Школа"), on_delete=models.CASCADE)
    number = models.IntegerField(_("Номер кабинета"))
    floor = models.IntegerField(_("Этаж (не обязательно)"), blank=True, null=True)
    name = models.CharField(_("Название кабинета (не обязательно)"), max_length=100, blank=True, null=True)
    employee = models.ForeignKey("school.Employees", verbose_name=_("Закрепленный педагог(не обязательно)"), on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'

    def __str__(self):
        return f'{self.number} | {self.name}'
    
