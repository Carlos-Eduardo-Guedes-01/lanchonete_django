# Generated by Django 4.1.3 on 2022-11-14 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lanchonete', '0006_alter_prato_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]