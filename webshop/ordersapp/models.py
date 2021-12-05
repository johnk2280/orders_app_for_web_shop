from django.db import models


class Customer(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    name = models.CharField(
        verbose_name='Имя',
        max_length=128,
        unique=True,
    )

    gender = models.CharField(
        verbose_name='Пол',
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        verbose_name='Заказчик',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    total_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return f'{self.created_at} - {self.customer} - {self.total_cost}'
