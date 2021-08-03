from django.db import models
from lib.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=30, verbose_name='name')
    cover = models.ImageField(upload_to='images/category/cover', verbose_name='cover')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_table = 'category'
