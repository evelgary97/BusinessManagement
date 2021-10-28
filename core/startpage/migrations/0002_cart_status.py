# Generated by Django 3.2.5 on 2021-10-18 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('sold', 'Sold')], default='pending', max_length=50, verbose_name='Status'),
        ),
    ]
