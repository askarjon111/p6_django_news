from django.shortcuts import render

from news.models import New, Category
from django.shortcuts import get_object_or_404

def news_list_view(request):
    news = New.objects.all()
    categories = Category.objects.all()

    context = {
        'latest_news': news,
        'categories': categories
    }
    return render(request, 'index.html', context)


def news_detail_view(request, pk):
    news = get_object_or_404(New, id=pk)
    context = {
        'news': news
    }
    return render(request, 'news_detail.html', context)
