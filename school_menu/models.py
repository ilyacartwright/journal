from django.db import models
from settings.models import Schools
from django.utils.translation import gettext as _


class Menu(models.Model):
    school = models.ForeignKey("settings.Schools", verbose_name=_("Школа"), on_delete=models.CASCADE)
    title = models.CharField(_("Название пункта меню"), max_length=50, help_text=_('Названия пункта выподающего меню'))
    sort = models.IntegerField(_("Номер отображения"), blank=True, null=True, default=1)
    is_active = models.BooleanField(_("Активный?"))

    class Meta:
        verbose_name = "Меню шапки сайта"
        verbose_name_plural = "Меню шапки сайта"
        ordering = ['sort']

    def __str__(self):
        return f"{self.school}"



class MenuItems(models.Model):
    menu = models.ForeignKey("school_menu.Menu", verbose_name=_("Партнер"), on_delete=models.CASCADE)
    title = models.CharField(_("Название"), max_length=50)
    link = models.CharField(_("Ссылка"), max_length=100)
    sort = models.IntegerField(_("Номер отображения"), blank=True, null=True, default=1)
    is_active = models.BooleanField(_("Активный?"))
    is_new_tab = models.BooleanField(_("Открывать в новой вкладке?"))

    class Meta:
        ordering = ['sort']