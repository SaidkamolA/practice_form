from django.db import models as mod


# Create your models here.

class Category(mod.Model):
    name = mod.CharField("Name", max_length=50)
    slug = mod.CharField("Slug", max_length=70)

    # description = mod.TextField("Description", null=True, unique=True)
    # bul = mod.BooleanField('Bul')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Item(mod.Model):
    name = mod.CharField(verbose_name="Name", max_length=70)
    slug = mod.CharField("Slug", max_length=90)
    description = mod.TextField("Description")
    price = mod.IntegerField('Price')
    count = mod.IntegerField('Count')
    category = mod.ForeignKey(Category, on_delete=mod.CASCADE)
    updated_at = mod.DateTimeField("Updated at", auto_now=True)

    def __str__(self):
        return f'''Id: {self.id}, 
        Name: {self.name}, 
        Desc: {self.description}, 
        Count: {self.count}, 
        Price: {self.price}'''

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']
