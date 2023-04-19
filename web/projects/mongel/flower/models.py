from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    is_published = models.BooleanField(verbose_name='Опубликован в шапке')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_id": self.pk})
    
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name',]

class Occasion(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    is_published = models.BooleanField(verbose_name='Опубликован в шапке')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("occasion", kwargs={"occ_id": self.pk})
    
    class Meta:
        verbose_name = 'Повод'
        verbose_name_plural = 'Поводы'
        ordering = ['name',]

class Season(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    is_published = models.BooleanField(verbose_name='Опубликован в шапке')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("season", kwargs={"sea_id": self.pk})
    
    class Meta:
        verbose_name = 'Время года'
        verbose_name_plural = 'Времена года'
        ordering = ['name',]

class Type(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    is_published = models.BooleanField(verbose_name='Опубликован в шапке')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("type", kwargs={"typ_id": self.pk})
    
    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'
        ordering = ['name',]
        

class Flower(models.Model):
    #-------------------------------main----------------------------------------- (not none)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    currency = models.CharField(max_length=255, verbose_name='Валюта')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    
    #---------------------------description-------------------------------------- (may none)
    size_height = models.DecimalField(max_digits=5, decimal_places=2, null=True, verbose_name='Высота товара')
    size_width = models.DecimalField(max_digits=5, decimal_places=2, null=True, verbose_name='Ширина товара')
    description_content = models.TextField(blank=True, null=True, verbose_name='Описание')
    new_product = models.BooleanField(verbose_name='Новинка')

    #-------------------------auto_documentation--------------------------------- (not none)
    time_create = models.DateTimeField(auto_now_add=True,verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    #-------------------------------links---------------------------------------- (may none)
    categ = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория товара')
    reason_data = models.ForeignKey(Occasion, on_delete=models.CASCADE, null=True, verbose_name='Повод')
    maturation_data = models.ForeignKey(Season, on_delete=models.CASCADE, null=True, verbose_name='Время созревания')
    type_data =  models.ForeignKey(Type, on_delete=models.CASCADE, null=True, verbose_name='Тип')
    
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['time_create', 'title']
    
class Review(models.Model):
    mark = models.IntegerField(verbose_name='Оценка товара')
    review_description = models.TextField(blank=True, verbose_name='Описание отзыва')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name='Товар')

    def __str__(self):
        return str(self.mark)
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['time_create', 'mark']
    
class Composition(models.Model):
    flower_part_1 = models.CharField(max_length=255, verbose_name='1 часть товара')
    flower_part_2 = models.CharField(max_length=255, verbose_name='2 часть товара')
    flower_part_3 = models.CharField(max_length=255, verbose_name='3 часть товара')
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name='Товар')

    def __str__(self):
        return self.flower_part_1
    
    class Meta:
        verbose_name = 'Состав букета'
        verbose_name_plural = 'Состав букета'
        ordering = ['flower',]
    
class Wrapping(models.Model):
    wrapping_part_1 = models.CharField(max_length=255, verbose_name='1 часть упаковки')
    wrapping_part_2 = models.CharField(max_length=255, verbose_name='2 часть упаковки')
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name='Товар')

    def __str__(self):
        return self.wrapping_part_1
    
    class Meta:
        verbose_name = 'Состав упаковки'
        verbose_name_plural = 'Состав упаковки'
        ordering = ['flower',]
