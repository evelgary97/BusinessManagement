# Generated by Django 3.2.5 on 2021-10-26 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0007_auto_20211018_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date_joined',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]