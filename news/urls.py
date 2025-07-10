from django.urls import path

from news.views import news_list_view, news_detail_view

urlpatterns = [
    path('', news_list_view, name='home'),
    path('news/<int:pk>/', news_detail_view, name='news_detail'),
]
