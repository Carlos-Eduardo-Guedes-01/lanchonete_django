# Generated by Django 4.1.3 on 2022-11-14 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lanchonete', '0008_alter_categoria_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prato',
            name='categoria',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='lanchonete.categoria'),
            preserve_default=False,
        ),
    ]