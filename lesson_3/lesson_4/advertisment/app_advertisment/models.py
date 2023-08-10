from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import  get_user_model

User = get_user_model()

class Advertisement(models.Model):#models.Model - это абстрактный класс-модель
    title = models.CharField('Название', max_length=128, )# ссылка на документацию https://django.fun/ru/docs/django/4.1/ref/models/fields/
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    @admin.display(description='Дата создания')
    def created(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time()
            return format_html(
                '<span>Сегодня в </span>', created_time
            )
        return self.created_at.strtime('%d.%m.%Y. в %H:%M:%S')

    def __str__(self):
        return f"Adtisement(id{self.id},title={self.title},price={self.price})"

    class Metta:
        db_table = "advertisements"
# Create your models here.
