import datetime

from rest_framework import serializers
from common.models import Cat, Breed
from dateutil.relativedelta import relativedelta

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = [
            'id',
            'title'
        ]


class CatSerializer(serializers.ModelSerializer):
    age = serializers.CharField()

    class Meta:
        model = Cat
        fields = [
            'id',
            'title',
            'breed',
            'photo',
            'desc',
            'age',
            'created_at'
        ]

    def validate_age(self, value):
        now = datetime.datetime.now().date()
        new_value = now + relativedelta(months=-int(value))
        return new_value



    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['age'] = "{} месяца".format(instance.age_to_month)
        context['breed'] = BreedSerializer(instance.breed).data
        return context
