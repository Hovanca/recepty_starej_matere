# Generated by Django 3.2.9 on 2022-02-24 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recepty_list', '0004_recept_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recept',
            name='ingredients',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Ingredients', to='recepty_list.ingredients'),
        ),
    ]
