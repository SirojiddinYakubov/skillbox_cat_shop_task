from django.urls import path
from api.v1.common import views

app_name = 'common'

urlpatterns = [
    path('cat/list/', views.ListCatAPIView.as_view(), name='cat_list'),
    path('cat/create/', views.CreateCatAPIView.as_view(), name='cat_create'),
    path('cat/update/<int:pk>/', views.UpdateCatAPIView.as_view(), name='cat_update'),
    path('cat/detail/<int:pk>/', views.DetailCatAPIView.as_view(), name='cat_detail'),
    path('cat/delete/<int:pk>/', views.DeleteCatAPIView.as_view(), name='cat_delete'),
]
