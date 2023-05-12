from django.db import models
from django.utils.translation import gettext as _


class Employees(models.Model):
    identifier = models.CharField(_("Идентикификатор/Логин"), max_length=50)
    password = models.CharField(_("Пароль"), max_length=50)
    first_name = models.CharField(_("Имя"), max_length=50)
    last_name = models.CharField(_("Фамилия"), max_length=50)
    surname = models.CharField(_("Отчество"), max_length=50, blank=True, null=True)

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

