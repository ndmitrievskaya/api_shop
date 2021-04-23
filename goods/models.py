from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField('Category', related_name='goods')
    price = models.FloatField()
    is_published = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
