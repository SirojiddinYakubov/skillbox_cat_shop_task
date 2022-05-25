import datetime

import django_filters as filters
from django.db import models
from django.db.models.functions import ExtractMonth

from common.models import Cat


class CatFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")
    breed = filters.CharFilter(lookup_expr="icontains", field_name="breed__title")
    desc = filters.CharFilter(lookup_expr="icontains")
    age = filters.CharFilter(
        method='age_filter'
    )

    def age_filter(self, queryset, name, value):
        now = datetime.datetime.now().date()
        qs = queryset.annotate(
            age_month=models.ExpressionWrapper(
                ExtractMonth('age') - now.month,
                output_field=models.SmallIntegerField()
            )).filter(age_month=value)
        return qs

    class Meta:
        model = Cat
        fields = [
            'title',
            'breed',
            'age',
            'desc'
        ]
