# Generated by Django 3.2.6 on 2021-09-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='uylartranslation',
            name='qoshimchajxozlar',
            field=models.CharField(max_length=100, verbose_name="Qo'chimcha jixozlar"),
        ),
    ]