from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


class Employees(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = PhoneNumberField(_("Номер телефона:"), null=True, blank=True, unique=True)
    management = models.BooleanField(
        _("Сотрудник может иметь класное руководство?"), null=True, blank=True
    )
    is_administrator = models.BooleanField(_("Администратор?"), default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.user}"


class PlaceWork(models.Model):
    employees = models.ForeignKey(
        "Employees", verbose_name=_("Сотрудник"), on_delete=models.CASCADE
    )
    school = models.ForeignKey("settings.Schools", verbose_name=_("Школа"), on_delete=models.CASCADE)
    position = models.ManyToManyField("settings.Positions", verbose_name=_("Должность"))
    subject = models.ManyToManyField(
        "settings.AcademicSubjects", verbose_name=_("Предметы:")
    )


class Cabinet(models.Model):
    school = models.ForeignKey(
        "settings.Schools", verbose_name=_("Школа"), on_delete=models.CASCADE
    )
    number = models.IntegerField(_("Номер кабинета"))
    floor = models.IntegerField(_("Этаж (не обязательно)"), blank=True, null=True)
    name = models.CharField(
        _("Название кабинета (не обязательно)"), max_length=100, blank=True, null=True
    )
    employee = models.ForeignKey(
        "school.Employees",
        verbose_name=_("Закрепленный педагог(не обязательно)"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"

    def __str__(self):
        return f"{self.number} | {self.name}"


class Classes(models.Model):
    school = models.ForeignKey(
        "settings.Schools", verbose_name=_("Школа"), on_delete=models.CASCADE
    )
    number = models.IntegerField(_("Номер классы/группы"))

    def __str__(self):
        return f"{self.number}"

    class Meta:
        verbose_name = "Класс/группа"
        verbose_name_plural = "Классы/группы"


class Groups(models.Model):
    classes = models.ForeignKey(
        "school.Classes", verbose_name=_("Класс"), on_delete=models.CASCADE
    )
    letter = models.CharField(_("Буква/номер"), max_length=10)
    supervisor = models.ForeignKey(
        "school.Employees",
        verbose_name=_("Классный руководитель/Руководитель"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )


class Items(models.Model):
    classes = models.ForeignKey(
        "school.Classes", verbose_name=_("Класс"), on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        "settings.AcademicSubjects", verbose_name=_("Предмет"), on_delete=models.CASCADE
    )
    group = models.IntegerField(_("Номер группы (если есть)"), null=True, blank=True)
    teacher = models.ForeignKey(
        "school.Employees",
        verbose_name=_("Педагог"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
