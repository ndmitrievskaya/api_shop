# Generated by Django 3.2 on 2021-04-23 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='category',
            field=models.ManyToManyField(limit_choices_to=10, related_name='goods', to='goods.Category'),
        ),
    ]