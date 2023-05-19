from django.db import models
from settings.models import Schools
from django.utils.translation import gettext as _


def fields():
    school = models.ForeignKey("settings.Schools", verbose_name=_("Школа"), on_delete=models.CASCADE)
    title = models.CharField(_("Название пункта меню"), max_length=50, help_text=_('Названия пункта выподающего меню'))
    is_active = models.BooleanField(_("Активный?"))
    return school, title, is_active
    


class Partners(models.Model):
    school = models.ForeignKey("settings.Schools", verbose_name=_("Школа"), on_delete=models.CASCADE)
    title = models.CharField(_("Название пункта меню"), max_length=50, help_text=_('Названия пункта выподающего меню'))
    is_active = models.BooleanField(_("Активный?"))

    class Meta:
        verbose_name = "Меню партнер"
        verbose_name_plural = "Меню партнеры"

    def __str__(self):
        return f"{self.school}"



class PartnersItems(models.Model):
    partner = models.ForeignKey("school_menu.Partners", verbose_name=_("Партнер"), on_delete=models.CASCADE)
    title = models.CharField(_("Название"), max_length=50)
    link = models.CharField(_("Ссылка"), max_length=100)
    is_active = models.BooleanField(_("Активный?"))


class Sites(models.Model):
    school = models.ForeignKey("settings.Schools", verbose_name=_("Школа"), on_delete=models.CASCADE)
    title = models.CharField(_("Название пункта меню"), max_length=50, help_text=_('Названия пункта выподающего меню'))
    is_active = models.BooleanField(_("Активный?"))

    class Meta:
        verbose_name = "Меню cайты"
        verbose_name_plural = "Меню сайты"

    def __str__(self):
        return f"{self.school}"



class SitesItems(models.Model):
    sites = models.ForeignKey("school_menu.Sites", verbose_name=_("Cайты"), on_delete=models.CASCADE)
    title = models.CharField(_("Название"), max_length=50)
    link = models.CharField(_("Ссылка"), max_length=100)
    is_active = models.BooleanField(_("Активный?"))


