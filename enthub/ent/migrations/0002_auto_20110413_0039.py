# Generated by Django 2.1 on 2011-04-12 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='duration',
            field=models.PositiveIntegerField(choices=[('', '---------'), ('7', '1 Week'), ('14', '2 Weeks'), ('28', '3 Weeks'), ('31', '1 Month'), ('366', '1 Year')], default=10),
        ),
    ]
