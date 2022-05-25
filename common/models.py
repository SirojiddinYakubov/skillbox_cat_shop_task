import datetime

from dateutil.relativedelta import relativedelta
from django.db import models


class BaseModel(models.Model):
    """ Базовая модель для всех моделей """
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Breed(BaseModel):
    """ модель для породы """
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Cat(BaseModel):
    """ модель для котёнка """
    title = models.CharField(verbose_name="Название", max_length=100)
    breed = models.ForeignKey(to=Breed, verbose_name="Парода", on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name="Изображение", upload_to='cats/%Y/%m/%d')
    age = models.DateField(verbose_name="Возраст")
    desc = models.CharField(verbose_name="Описание", max_length=255)

    @property
    def age_to_month(self):
        now = datetime.datetime.now().date()
        r = relativedelta(now, self.age)
        return r.months + (12 * r.years)

    def __str__(self):
        return self.title
