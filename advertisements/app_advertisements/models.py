from django.db import models


class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text='Отметьте, если торг уместен')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Advertisement(id={self.id}, price={self.price} , title={self.title})'

    class Meta:
        db_table = "advertisements"




