from django.urls import path

from news.views import add_news_view, delete_news_view, news_list_view, news_detail_view

urlpatterns = [
    path('', news_list_view, name='home'),
    path('news/<int:pk>/', news_detail_view, name='news_detail'),
    path('news/<int:pk>/delete', delete_news_view, name='news_delete'),
    path('news/add/', add_news_view, name='add_news'),
]
