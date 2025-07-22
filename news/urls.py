from django.urls import path

from news.views import AddNewsView, DeleteNewsView, NewsListView, NewsDetailView, NewsUpdateView

urlpatterns = [
    path('', NewsListView.as_view(), name='home'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', DeleteNewsView.as_view(), name='news_delete'),
    path('news/add/', AddNewsView.as_view(), name='add_news'),
]
