from rest_framework import generics

from api.v1.common import filters
from api.v1.common.serializers import CatSerializer
from common.models import Cat


class ListCatAPIView(generics.ListAPIView):
    """ список кошек """
    queryset = Cat.objects.filter(is_active=True)
    serializer_class = CatSerializer
    filter_class = filters.CatFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        order_param = self.request.GET.get('ordering', 'created_at')
        if order_param == 'breed':
            qs = queryset.order_by("breed__title")
        else:
            qs = queryset.order_by(order_param)
        return qs


class CreateCatAPIView(generics.CreateAPIView):
    """ создать кошку """
    queryset = Cat.objects.filter(is_active=True)
    serializer_class = CatSerializer


class UpdateCatAPIView(generics.UpdateAPIView):
    """ редактировать кота """
    queryset = Cat.objects.filter(is_active=True)
    serializer_class = CatSerializer


class DetailCatAPIView(generics.RetrieveAPIView):
    """ подробнее о коте """
    queryset = Cat.objects.filter(is_active=True)
    serializer_class = CatSerializer


class DeleteCatAPIView(generics.DestroyAPIView):
    """ удаление кота """
    queryset = Cat.objects.filter(is_active=True)
    serializer_class = CatSerializer
