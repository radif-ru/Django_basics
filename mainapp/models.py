from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя категории', max_length=128)
    description = models.TextField(verbose_name='описание категории', blank=True)
    modified_date = models.DateTimeField(
        verbose_name='дата изменения', auto_now=True)
    is_active = models.BooleanField(verbose_name='активность', default=True)

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'
        ordering = ['name']


class Product(models.Model):
    category = models.ForeignKey(ProductCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name='категория продукта')
    name = models.CharField('имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField('краткое описание продукта', max_length=64, blank=True)
    description = models.TextField('описание продукта', blank=True)
    price = models.DecimalField('цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField('количество на складе', default=0)
    modified_date = models.DateTimeField(
        verbose_name='дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.description}). ' \
               f'Категория - {self.category.name} ({self.category.description})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
