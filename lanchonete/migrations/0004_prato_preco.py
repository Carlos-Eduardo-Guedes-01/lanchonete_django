# Generated by Django 4.1.3 on 2022-11-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lanchonete', '0003_prato_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='prato',
            name='preco',
            field=models.FloatField(null=True),
        ),
    ]
