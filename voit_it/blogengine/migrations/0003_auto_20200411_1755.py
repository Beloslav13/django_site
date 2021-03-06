# Generated by Django 2.2.4 on 2020-04-11 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogengine', '0002_auto_20200402_2116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blogengine.Category', verbose_name='Категория'),
        ),
    ]
