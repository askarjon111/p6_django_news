from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from news.forms import AddNewsForm
from news.models import New

class NewsListView(ListView):
    queryset = New.objects.all()
    template_name = 'index.html'
    context_object_name = 'latest_news'


class NewsDetailView(DetailView):
    queryset = New.objects.all()
    template_name = 'news_detail.html'
    context_object_name = 'news'


class NewsUpdateView(UpdateView):
    queryset = New.objects.all()
    fields = ['title', 'content', 'image', 'category']

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('news_detail', kwargs={'pk': pk})


class AddNewsView(CreateView):
    queryset = New.objects.all()
    form_class = AddNewsForm
    template_name = 'add_news.html'


class DeleteNewsView(DeleteView):
    queryset = New.objects.all()
    success_url = ''
    template_name = 'news_deleted.html'

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy('news:news_delete')
