# Generated by Django 3.2.5 on 2021-09-29 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210929_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(blank=True, default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci consequatur corporis doloremque dolorum, eaque illo, illum, inventore iure maiores molestias pariatur porro qui quia quos ratione repudiandae suscipit tenetur totam. ', max_length=150, null=True, verbose_name='Product description'),
        ),
    ]
