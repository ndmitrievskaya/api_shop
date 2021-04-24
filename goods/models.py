from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, max_length=300)

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=300)
    categories = models.ManyToManyField(Category)
    price = models.FloatField()
    is_published = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
