# Generated by Django 4.2.2 on 2023-06-13 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='amount_of_money',
            field=models.CharField(max_length=30),
        ),
    ]