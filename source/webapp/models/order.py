from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                             verbose_name='Пользователь')
    first_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, null=False, blank=False, verbose_name='Телефон')
    email = models.EmailField(max_length=200, null=False, blank=False, verbose_name='Email')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = "order"
        verbose_name = "Заказ оформления"
        verbose_name_plural = "Заказы оформления"


class OrderPart(models.Model):
    order = models.ForeignKey('webapp.Order', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    part = models.ForeignKey('webapp.Part', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quantity} {self.part}'

    class Meta:
        db_table = "order_part"
