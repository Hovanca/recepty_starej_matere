# Generated by Django 3.2.9 on 2022-02-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepty_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recept',
            name='difficulty',
            field=models.CharField(choices=[('1', 'Low'), ('2', 'Medium'), ('3', 'High')], default='1', max_length=1),
        ),
    ]
