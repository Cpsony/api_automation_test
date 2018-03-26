# Generated by Django 2.0.2 on 2018-03-21 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0010_auto_20180320_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='automationresponsejson',
            name='tier',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='层级关系'),
        ),
        migrations.AlterField(
            model_name='automationresponsejson',
            name='name',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='JSON参数'),
        ),
    ]