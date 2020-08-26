from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя категории', max_length=128)
    description = models.TextField(verbose_name='описание категории', blank=True)

    def __str__(self):
        string = ''
        if self.id:
            string += f'\nid = {self.id}'
        if self.name:
            string += f'\nname = {self.name}'
        if self.description:
            string += f'\ndescription = {self.description}'
        return string

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name='категория продукта')
    name = models.CharField('имя продукта', max_length=128)
    # image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField('краткое описание продукта', max_length=64, blank=True)
    description = models.TextField('описание продукта', blank=True)
    price = models.DecimalField('цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField('количество на складе', default=0)

    def __str__(self):
        string = ''
        if self.id:
            string += f'\nid = {self.id}'
        if self.name:
            string += f'\nname = {self.name}'
        if self.short_desc:
            string += f'\nshort_desc = {self.short_desc}'
        if self.description:
            string += f'\ndescription = {self.description}'
        if self.price:
            string += f'\nprice = {self.price}'
        if self.quantity:
            string += f'\nquantity = {self.quantity}'
        if self.category:
            string += f'\ncategory_id = {self.category_id}'
            string += f'\n\n*ProductCategory.name = {self.category.name}'
            string += f'\n*ProductCategory.description = {self.category.description}'
        return string

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
