# Generated by Django 3.2 on 2021-04-23 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('price', models.FloatField()),
                ('is_published', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(related_name='goods', to='goods.Category')),
            ],
        ),
    ]
