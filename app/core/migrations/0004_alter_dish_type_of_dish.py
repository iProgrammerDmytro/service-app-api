# Generated by Django 3.2.13 on 2022-05-03 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220503_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='type_of_dish',
            field=models.CharField(choices=[('A', 'Appetizer'), ('MD', 'Main dish'), ('C', 'Cocktail')], default='MD', max_length=2),
        ),
    ]