# Generated by Django 4.1.4 on 2023-05-19 23:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school_menu", "0008_rename_new_tab_menuitems_is_new_tab"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="menu",
            options={
                "ordering": ["sort"],
                "verbose_name": "Меню шапки сайта",
                "verbose_name_plural": "Меню шапки сайта",
            },
        ),
        migrations.AlterModelOptions(
            name="menuitems",
            options={"ordering": ["sort"]},
        ),
        migrations.AddField(
            model_name="menu",
            name="sort",
            field=models.IntegerField(
                blank=True, default=1, null=True, verbose_name="Номер отображения"
            ),
        ),
        migrations.AddField(
            model_name="menuitems",
            name="sort",
            field=models.IntegerField(
                blank=True, default=1, null=True, verbose_name="Номер отображения"
            ),
        ),
    ]