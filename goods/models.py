from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, through='GoodCategory',
                                      through_fields=('good', 'category'),
                                      on_delete=models.SET_NULL)
    price = models.DecimalField()
    is_published = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)


class GoodCategory(models.Model):
    good = models.ForeignKey(Good, related_name='good_category',
                             on_delete=models.CASCADE)
    category = models.ForeignKey(Category, )
