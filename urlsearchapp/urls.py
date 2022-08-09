from django.urls import path
from . import views
from .views import ItemDelete  # ビューの読み込み

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('history/', views.history, name='history'),
    path('delete/<int:pk>', ItemDelete.as_view(), name='delete'),  # 削除機能

]
