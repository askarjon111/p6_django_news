from django.shortcuts import redirect, render
from django.urls import reverse

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


def add_news_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = {
            'categories': categories
        }
        return render(request, 'add_news.html', data)
    elif request.method == 'POST':
        category = Category.objects.get(id=request.POST.get('category'))
        title = request.POST.get('title')
        image = request.FILES.get('image')
        content = request.POST.get('content')
        news = New.objects.create(title=title,
                                  category=category,
                                  image=image,
                                  content=content)
        return redirect(reverse('news_detail', kwargs={'pk': news.id}))
