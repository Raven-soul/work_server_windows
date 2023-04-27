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
        verbose_name = '1. Категория'
        verbose_name_plural = '1. Категории'
        ordering = ['name',]

class Occasion(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    is_published = models.BooleanField(verbose_name='Опубликован в шапке')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("occasion", kwargs={"occ_id": self.pk})
    
    class Meta:
        verbose_name = '1. Повод'
        verbose_name_plural = '1. Поводы'
        ordering = ['name',]

class Season(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    is_published = models.BooleanField(verbose_name='Опубликован в шапке')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("season", kwargs={"sea_id": self.pk})
    
    class Meta:
        verbose_name = '1. Время года'
        verbose_name_plural = '1. Времена года'
        ordering = ['name',]

class Type(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    is_published = models.BooleanField(verbose_name='Опубликован в шапке')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("type", kwargs={"typ_id": self.pk})
    
    class Meta:
        verbose_name = '1. Тип товара'
        verbose_name_plural = '1. Типы товаров'
        ordering = ['name',]
        

class Flower(models.Model):
    #-------------------------------main----------------------------------------- (not none)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    currency = models.CharField(max_length=255, verbose_name='Валюта')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    count = models.IntegerField(verbose_name='Кол-во товара на складе')
    
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
    
    def get_absolute_url(self):
        return reverse("product", kwargs={"prod_id": self.pk})
    
    class Meta:
        verbose_name = '1. Товар'
        verbose_name_plural = '1. Товары'
        ordering = ['time_create', 'title']
    
class Review(models.Model):
    grade = models.IntegerField(verbose_name='Оценка товара')
    description = models.TextField(blank=True, verbose_name='Описание отзыва')
    author = models.CharField(max_length=255, null=True, verbose_name='Автор отзыва')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name='Товар')

    def __str__(self):
        return str(self.grade)
    
    class Meta:
        verbose_name = '2. Отзыв'
        verbose_name_plural = '2. Отзывы'
        ordering = ['time_create', 'grade']
    
class Composition(models.Model):
    flower_part_1 = models.CharField(max_length=255, verbose_name='1 часть товара')
    flower_part_2 = models.CharField(max_length=255, verbose_name='2 часть товара')
    flower_part_3 = models.CharField(max_length=255, verbose_name='3 часть товара')
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name='Товар')

    def __str__(self):
        return self.flower_part_1
    
    class Meta:
        verbose_name = '2. Состав букета'
        verbose_name_plural = '2. Состав букета'
        ordering = ['flower',]
    
class Wrapping(models.Model):
    wrapping_part_1 = models.CharField(max_length=255, verbose_name='1 часть упаковки')
    wrapping_part_2 = models.CharField(max_length=255, verbose_name='2 часть упаковки')
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name='Товар')

    def __str__(self):
        return self.wrapping_part_1
    
    class Meta:
        verbose_name = '2. Состав упаковки'
        verbose_name_plural = '2. Состав упаковки'
        ordering = ['flower',]

class InfoClass(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название группы')
    name_code = models.CharField(max_length=255, verbose_name='Код группы')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '3. Класс инфо-страницы'
        verbose_name_plural = '3. Класс инфо-страниц'
        ordering = ['id',]

class InfoPages(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название страницы')
    path = models.CharField(max_length=255, verbose_name='Путь страницы')
    order = models.IntegerField(verbose_name='Очередь столбца')
    classificate = models.ForeignKey(InfoClass, on_delete=models.CASCADE, null=True, verbose_name='Класс')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '3. Инфо-страница'
        verbose_name_plural = '3. Инфо-страницы'
        ordering = ['id',]

class User(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.CharField(unique=True, max_length=255, verbose_name='Логин')
    password = models.CharField(max_length=255, verbose_name='Пароль')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '4. Пользователь'
        verbose_name_plural = '4. Пользователи'
        ordering = ['id',]

class Register_form(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.CharField(unique=True, max_length=255, verbose_name='Логин')
    password_first = models.CharField(max_length=255, verbose_name='Пароль')
    password_second = models.CharField(max_length=255, verbose_name='Повтор пароля')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '4. Форма регистрации'
        verbose_name_plural = '4. Форма регистрации'
        ordering = ['id',]

class SelectedProducts(models.Model):
    sesseion_id = models.CharField(max_length=255, verbose_name='Код сессии') 
    count = models.IntegerField(verbose_name='Количество товара')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name='Товар')

    def __str__(self):
        return self.sesseion_id
    
    class Meta:
        verbose_name = '5. Список выбранных товаров'
        verbose_name_plural = '5. Список выбранных товаров'
        ordering = ['id',]