from django.shortcuts import redirect, render
from django.urls import reverse

from news.forms import AddNewsForm
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
    categories = Category.objects.all()
    context = {
        'news': news,
        'categories': categories,
    }
    if request.method == 'POST':
        news.category = Category.objects.get(id=request.POST.get('category'))
        news.title = request.POST.get('title')
        if request.FILES.get('image'):
            news.image = request.FILES.get('image')
        news.content = request.POST.get('content')
        news.save()
    return render(request, 'news_detail.html', context)


def add_news_view(request):
    if request.method == 'GET':
        news_form = AddNewsForm()
        categories = Category.objects.all()
        data = {
            'categories': categories,
            'news_form': news_form,
        }
        return render(request, 'add_news.html', data)
    elif request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect(reverse('home'))


def delete_news_view(request, pk):
    news = New.objects.get(id=pk)
    news.delete()
    return render(request, 'news_deleted.html')
